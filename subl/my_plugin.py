import sublime
import sublime_plugin

# change the default save directory to desktop
class CustomSaveCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		# change 'user_name'
		self.view.settings().set("default_dir", "/Users/user_name/desktop")
		self.view.run_command("save")
