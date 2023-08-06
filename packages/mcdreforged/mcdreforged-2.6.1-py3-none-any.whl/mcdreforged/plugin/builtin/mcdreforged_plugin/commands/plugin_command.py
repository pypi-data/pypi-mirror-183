import os
from typing import TYPE_CHECKING, Callable, List, Tuple, Any

from mcdreforged.command.builder.nodes.arguments import QuotableText
from mcdreforged.command.builder.nodes.basic import Literal
from mcdreforged.command.command_source import CommandSource
from mcdreforged.minecraft.rtext.style import RColor, RStyle, RAction
from mcdreforged.minecraft.rtext.text import RTextList, RText
from mcdreforged.permission.permission_level import PermissionLevel
from mcdreforged.plugin.builtin.mcdreforged_plugin.commands.sub_command import SubCommand
from mcdreforged.plugin.type.plugin import AbstractPlugin
from mcdreforged.plugin.type.regular_plugin import RegularPlugin

if TYPE_CHECKING:
	from mcdreforged.plugin.builtin.mcdreforged_plugin.mcdreforged_plugin import MCDReforgedPlugin


class PluginCommand(SubCommand):
	def __init__(self, mcdr_plugin: 'MCDReforgedPlugin'):
		super().__init__(mcdr_plugin)
		self.plugin_manager = self.mcdr_server.plugin_manager

	def get_command_node(self) -> Literal:
		def plugin_id_node():
			return QuotableText('plugin_id').suggests(lambda: [plg.get_id() for plg in self.plugin_manager.get_regular_plugins()])

		def unloaded_plugin_node():
			return QuotableText('file_name').suggests(lambda: map(os.path.basename, self.server_interface.get_unloaded_plugin_list()))

		def disabled_plugin_node():
			return QuotableText('file_name').suggests(lambda: map(os.path.basename, self.server_interface.get_disabled_plugin_list()))

		return (
			self.control_command_root({'plugin', 'plg'}).
			runs(lambda src: src.reply(self.get_help_message(src, 'mcdr_command.help_message.plugin'))).
			then(Literal('list').runs(self.list_plugin)).
			then(Literal('info').then(plugin_id_node().runs(lambda src, ctx: self.show_plugin_info(src, ctx['plugin_id'])))).
			then(Literal('load').then(unloaded_plugin_node().runs(lambda src, ctx: self.load_plugin(src, ctx['file_name'])))).
			then(Literal('enable').then(disabled_plugin_node().runs(lambda src, ctx: self.enable_plugin(src, ctx['file_name'])))).
			then(Literal('reload').then(plugin_id_node().runs(lambda src, ctx: self.reload_plugin(src, ctx['plugin_id'])))).
			then(Literal('unload').then(plugin_id_node().runs(lambda src, ctx: self.unload_plugin(src, ctx['plugin_id'])))).
			then(Literal('disable').then(plugin_id_node().runs(lambda src, ctx: self.disable_plugin(src, ctx['plugin_id'])))).
			then(Literal({'reloadall', 'ra'}).runs(self.reload_all_plugin))
		)

	def list_plugin(self, source: CommandSource):
		not_loaded_plugin_list: List[str] = self.server_interface.get_unloaded_plugin_list()
		disabled_plugin_list: List[str] = self.server_interface.get_disabled_plugin_list()
		current_plugins = list(self.mcdr_server.plugin_manager.get_all_plugins())  # type: List[AbstractPlugin]

		source.reply(self.tr('mcdr_command.list_plugin.info_loaded_plugin', len(current_plugins)))
		for plugin in current_plugins:
			meta = plugin.get_metadata()
			displayed_name = RText(meta.name)
			if not self.can_see_rtext(source):
				displayed_name += RText(' ({})'.format(plugin.get_identifier()), color=RColor.gray)
			texts = RTextList(
				'§7-§r ',
				displayed_name.
				c(RAction.run_command, '{} plugin info {}'.format(self.control_command_prefix, meta.id)).
				h(self.tr('mcdr_command.list_plugin.suggest_info', plugin.get_identifier()))
			)
			if self.can_see_rtext(source) and not plugin.is_permanent():
				texts.append(
					' ',
					RText('[↻]', color=RColor.gray)
					.c(RAction.run_command, '{} plugin reload {}'.format(self.control_command_prefix, meta.id))
					.h(self.tr('mcdr_command.list_plugin.suggest_reload', meta.id)),
					' ',
					RText('[↓]', color=RColor.gray)
					.c(RAction.run_command, '{} plugin unload {}'.format(self.control_command_prefix, meta.id))
					.h(self.tr('mcdr_command.list_plugin.suggest_unload', meta.id)),
					' ',
					RText('[×]', color=RColor.gray)
					.c(RAction.run_command, '{} plugin disable {}'.format(self.control_command_prefix, meta.id))
					.h(self.tr('mcdr_command.list_plugin.suggest_disable', meta.id))
				)
			source.reply(texts)

		def get_file_name(fp) -> Tuple[str, RText]:
			name = os.path.basename(fp)
			name_text = RText(name)
			if source.has_permission(PermissionLevel.PHYSICAL_SERVER_CONTROL_LEVEL):
				name_text.h(fp)
			return name, name_text

		source.reply(self.tr('mcdr_command.list_plugin.info_disabled_plugin', len(disabled_plugin_list)))
		for file_path in disabled_plugin_list:
			file_name, file_name_text = get_file_name(file_path)
			texts = RTextList(RText('- ', color=RColor.gray), file_name_text)
			if self.can_see_rtext(source):
				texts.append(
					' ',
					RText('[✔]', color=RColor.gray)
					.c(RAction.run_command, '{} plugin enable {}'.format(self.control_command_prefix, file_name))
					.h(self.tr('mcdr_command.list_plugin.suggest_enable', file_name))
				)
			source.reply(texts)

		source.reply(self.tr('mcdr_command.list_plugin.info_not_loaded_plugin', len(not_loaded_plugin_list)))
		for file_path in not_loaded_plugin_list:
			file_name, file_name_text = get_file_name(file_path)
			texts = RTextList(RText('- ', color=RColor.gray), file_name_text)
			if self.can_see_rtext(source):
				texts.append(
					' ',
					RText('[↑]', color=RColor.gray)
					.c(RAction.run_command, '{} plugin load {}'.format(self.control_command_prefix, file_name))
					.h(self.tr('mcdr_command.list_plugin.suggest_load', file_name))
				)
			source.reply(texts)

	def show_plugin_info(self, source: CommandSource, plugin_id: str):
		plugin = self.mcdr_server.plugin_manager.get_plugin_from_id(plugin_id)
		if plugin is None:
			source.reply(self.tr('mcdr_command.invalid_plugin_id', plugin_id))
		else:
			meta = plugin.get_metadata()
			source.reply(RTextList(
				RText(meta.name).set_color(RColor.yellow).set_styles(RStyle.bold).h(plugin),
				' ',
				RText('v{}'.format(meta.version), color=RColor.gray)
			))
			source.reply(self.tr('mcdr_command.plugin_info.id', meta.id))
			if meta.author is not None:
				source.reply(self.tr('mcdr_command.plugin_info.author', ', '.join(meta.author)))
			if meta.link is not None:
				source.reply(self.tr('mcdr_command.plugin_info.link', RText(meta.link, color=RColor.blue, styles=RStyle.underlined).c(RAction.open_url, meta.link)))
			if meta.description is not None:
				source.reply(meta.get_description_rtext())

	def __not_loaded_plugin_file_manipulate(self, source: CommandSource, file_name: str, operation_name: str, func: Callable[[str], Any], possible_plugin_path: List[str]):
		plugin_paths = list(filter(lambda fp: fp == file_name, possible_plugin_path))
		if len(plugin_paths) == 0:
			plugin_paths = list(filter(lambda fp: os.path.basename(fp) == file_name, possible_plugin_path))
		if len(plugin_paths) == 0:
			source.reply(self.tr('mcdr_command.invalid_plugin_file_name', file_name))
		else:
			result = self.function_call(source, lambda: func(plugin_paths[0]), operation_name, log_success=False, msg_args=(file_name,))
			if result.return_value is True:
				source.reply(self.tr('mcdr_command.{}.success'.format(operation_name), file_name))
			else:
				source.reply(self.tr('mcdr_command.{}.fail'.format(operation_name), file_name))
			self._print_plugin_operation_result_if_no_error(source, result)

	def __existed_regular_plugin_manipulate(self, source: CommandSource, plugin_id: str, operation_name: str, func: Callable[[RegularPlugin], Any]):
		plugin = self.mcdr_server.plugin_manager.get_regular_plugin_from_id(plugin_id)
		if plugin is None or not plugin.is_regular():
			source.reply(self.tr('mcdr_command.invalid_plugin_id', plugin_id))
		else:
			result = self.function_call(source, lambda: func(plugin), operation_name, log_success=False, msg_args=(plugin.get_name(),))
			if result.return_value is True:
				source.reply(self.tr('mcdr_command.{}.success'.format(operation_name), plugin.get_name()))
			else:
				source.reply(self.tr('mcdr_command.{}.fail'.format(operation_name), plugin.get_name()))
			self._print_plugin_operation_result_if_no_error(source, result)

	def disable_plugin(self, source: CommandSource, plugin_id: str):
		self.__existed_regular_plugin_manipulate(source, plugin_id, 'disable_plugin', lambda plg: self.server_interface.disable_plugin(plg.get_id()))

	def reload_plugin(self, source: CommandSource, plugin_id: str):
		self.__existed_regular_plugin_manipulate(source, plugin_id, 'reload_plugin', lambda plg: self.server_interface.reload_plugin(plg.get_id()))

	def unload_plugin(self, source: CommandSource, plugin_id: str):
		self.__existed_regular_plugin_manipulate(source, plugin_id, 'unload_plugin', lambda plg: self.server_interface.unload_plugin(plg.get_id()))

	def load_plugin(self, source: CommandSource, file_name: str):
		self.__not_loaded_plugin_file_manipulate(source, file_name, 'load_plugin', lambda pth: self.server_interface.load_plugin(pth), self.server_interface.get_unloaded_plugin_list())

	def enable_plugin(self, source: CommandSource, file_name: str):
		self.__not_loaded_plugin_file_manipulate(source, file_name, 'enable_plugin', lambda pth: self.server_interface.enable_plugin(pth), self.server_interface.get_disabled_plugin_list())

	def reload_all_plugin(self, source: CommandSource):
		ret = self.function_call(source, self.mcdr_server.plugin_manager.refresh_all_plugins, 'reload_all_plugin', log_success=False)
		self._print_plugin_operation_result_if_no_error(source, ret)
