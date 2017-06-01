#!/usr/bin/env python

import argparse
import defaults
import helpers

def gen_root_folder(project_name):
	""
	path = defaults.PROJECTS_PATH
	commands = [
		["mkdir", project_name]
	]
	helpers.execute_commands(commands, path)

def gen_p4(project_name):
	""
	path = defaults.PROJECTS_PATH + project_name + "/"
	commands = [
		["mkdir", defaults.PROJECT_P4_NAME]
	]
	helpers.execute_commands(commands, path)

def gen_util(project_name):
	""
	path = defaults.PROJECTS_PATH + project_name + "/"
	commands = [
		["mkdir", defaults.PROJECT_UTIL_NAME]
	]
	helpers.execute_commands(commands, path)

def gen_tools(project_name):
	""
	path = defaults.PROJECTS_PATH + project_name + "/"
	commands = [
		["mkdir", defaults.PROJECT_TOOLS_NAME]
	]
	helpers.execute_commands(commands, path)

def gen_mininet(project_name):
	""
	path = defaults.PROJECTS_PATH + project_name + "/"
	commands = [
		["mkdir", defaults.PROJECT_MININET_NAME]
	]
	helpers.execute_commands(commands, path)

def gen_build(project_name):
	""
	path = defaults.PROJECTS_PATH + project_name + "/"
	commands = [
		["mkdir", defaults.PROJECT_BUILD_NAME]
	]
	helpers.execute_commands(commands, path)

def gen_images(project_name):
	""
	path = defaults.PROJECTS_PATH + project_name + "/"
	commands = [
		["mkdir", defaults.PROJECT_IMAGES_NAME]
	]
	helpers.execute_commands(commands, path)

def gen_template_file(file, context, path):
	""
	template = helpers.render_template(file, context)
	commands = [
		["touch", file]
	]
	helpers.execute_commands(commands, path)
	helpers.write_file(path + file, template)

def gen_file(file, path):
	""
	commands = [
		["touch", file]
	]
	helpers.execute_commands(commands, path)	

def gen_root_files(project_name):
	""
	path = defaults.PROJECTS_PATH + project_name + "/"
	template_files = ["DOC.md"]
	context = {'project_name' : project_name}

	for file in template_files:
		gen_template_file(file, context, path)

def gen_p4_files(project_name):
	""
	path = defaults.PROJECTS_PATH + project_name + "/" + defaults.PROJECT_P4_NAME
	files = [project_name + ".p4"]

	for file in files:
		gen_file(file, path)

def gen_util_files(project_name):
	""
	path = defaults.PROJECTS_PATH + project_name + "/" + defaults.PROJECT_UTIL_NAME
	files = [defaults.PROJECT_COMMANDS_NAME]

	for file in files:
		gen_file(file, path)

def gen_tools_files(project_name):
	""
	path = defaults.PROJECTS_PATH + project_name + "/" + defaults.PROJECT_TOOLS_NAME
	template_files = ["apply_commands.py", "build_project.py", "run_cli.py", "run_project.py"]
	context = {'project_name' : project_name}

	for file in template_files:
		gen_template_file(file, context, path)

def gen_mininet_files(project_name):
	""
	path = defaults.PROJECTS_PATH + project_name + "/" + defaults.PROJECT_MININET_NAME
	files = [project_name + ".py"]

	for file in files:
		gen_file(file, path)

def gen_folders(project_name):
	""
	gen_root_folder(project_name)
	gen_p4(project_name)
	gen_util(project_name)
	gen_tools(project_name)
	gen_mininet(project_name)
	gen_build(project_name)
	gen_images(project_name)

def gen_files(project_name):
	""
	gen_root_files(project_name)
	gen_p4_files(project_name)
	gen_util_files(project_name)
	gen_tools_files(project_name)
	gen_mininet_files(project_name)

def gen_project(args):
	""
	gen_folders(args.project_name)
	gen_files(args.project_name)

def get_args():
	"" 
	parser = argparse.ArgumentParser(description = 'Generates a new project workspace.')
	parser.add_argument('project_name', help = "Name of the project.")
	return parser.parse_args()

if __name__ == '__main__':

	args = get_args()
	gen_project(args)