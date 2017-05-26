#!/usr/bin/env python

import defaults
import helpers

def gen_root_folder(project_name):
	""
	commands = [
		["mkdir", project_name]
	]
	helpers.execute_commands(commands, defaults.PROJECTS_DIR)

def gen_p4(project_name):
	""
	commands = [
		["mkdir", defaults.PROJECT_P4_NAME]
	]
	helpers.execute_commands(commands, defaults.PROJECTS_DIR + project_name)

def gen_util(project_name):
	""
	commands = [
		["mkdir", defaults.PROJECT_UTIL_NAME]
	]
	helpers.execute_commands(commands, defaults.PROJECTS_DIR + project_name)

def gen_tools(project_name):
	""
	commands = [
		["mkdir", defaults.PROJECT_TOOLS_NAME]
	]
	helpers.execute_commands(commands, defaults.PROJECTS_DIR + project_name)

def gen_mininet(project_name):
	""
	commands = [
		["mkdir", defaults.PROJECT_MININET_NAME]
	]
	helpers.execute_commands(commands, defaults.PROJECTS_DIR + project_name)

def gen_file(file, context, path):
	""
	template = helpers.render_template(file, context)
	commands = [
		["touch", file],
		["echo", template, ">", file]
	]
	helpers.execute_commands(commands, path)

def gen_root_files(project_name):
	""
	files = ["README.md"]
	context = {'project_name' : project_name}
	path = defaults.PROJECTS_DIR + project_name

	for file in files:
		gen_file(file, context, path)

def gen_folders(project_name):
	""
	gen_root_folder(project_name)
	gen_p4(project_name)
	gen_util(project_name)
	gen_tools(project_name)
	gen_mininet(project_name)

def gen_files(project_name):
	""
	gen_root_files(project_name)

if __name__ == '__main__':
	
	gen_folders("teste")
	gen_files("teste")