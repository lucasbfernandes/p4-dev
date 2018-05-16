#!/usr/bin/env python

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../../core/tools/")

import defaults
import helpers

def apply_commands(project_name):
	""
	path = defaults.PROJECTS_PATH + project_name + "/"
	comandos = open(path + defaults.PROJECT_UTIL_NAME + defaults.PROJECT_COMMANDS_NAME).readlines()
	helpers.execute_commands(defaults.PROJECT_BUILD_NAME + project_name + ".json", "localhost", 9090, comandos)

if __name__ == '__main__':

	apply_commands("direct_flow_counter")