#!/usr/bin/env python

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../../core/tools/")

import defaults
import helpers

def run_cli(project_name):
	""
	path = defaults.PROJECTS_PATH + project_name + "/"
	commands = [
		[
			defaults.BMV2_CLI_PATH,
			defaults.PROJECT_BUILD_NAME + project_name + ".json"
		]
	]
	helpers.execute_commands(commands, path)

if __name__ == '__main__':

	run_cli("probabilistic-drop-multipath")