#!/usr/bin/env python

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../../core/tools/")

import defaults
import helpers

def apply_commands(project_name):
	""
	path = defaults.PROJECTS_PATH + project_name + "/"
	stdin = open(path + defaults.PROJECT_UTIL_NAME + defaults.PROJECT_COMMANDS_NAME)
	commands = [
		[
			defaults.BMV2_CLI_PATH,
			defaults.PROJECT_BUILD_NAME + project_name + ".json"
		]
	]
	helpers.execute_commands(commands, path, stdin)

if __name__ == '__main__':

	apply_commands("multi-path-routing")