#!/usr/bin/env python

import defaults
import helpers

def gen_root_folder():
	""
	commands = [
		["sudo", "pip", "install", "-r", "requirements.txt"],
		["sudo", "python", "setup.py", "install"],
	]
	helpers.execute_commands(commands, defaults.PROJECTS_DIR)

def gen_p4():
	pass

def gen_util():
	pass

def gen_tools():
	pass

def gen_mininet():
	pass

def gen_root_files():
	""
	commands = [
		["sudo", "pip", "install", "-r", "requirements.txt"],
		["sudo", "python", "setup.py", "install"],
	]
	helpers.execute_commands(commands, defaults.P4C_BM_DIR)

def gen_folders:
	pass

if __name__ == '__main__':
	pass