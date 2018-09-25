import sublime, sublime_plugin
import os


class CustomNewSnippetCommand(sublime_plugin.WindowCommand):
    def run(self):
        v = self.window.new_file()
        v.settings().set('default_dir',
          os.path.join(sublime.packages_path(), 'User'))
        v.settings().set('default_extension', 'sublime-snippet')
        v.set_syntax_file('Packages/XML/XML.tmLanguage')

        template = """<snippet>
	
	<content><![CDATA[
		Replace your snippet content
	]]></content>
	<tabTrigger>${3:$2}</tabTrigger>
	<!--  ${num:${TM_FILENAME/(.+)..+./$num/}} file name without extension-->
	<scope>source.scopeHere</scope>
	<description>$2</description>
</snippet>
"""
        v.run_command("insert_snippet", {"contents": template})
