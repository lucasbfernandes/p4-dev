#!/usr/bin/env python

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../../core/tools/")

import defaults
import helpers

def gen_project_json(project_name):
	""
	path = defaults.PROJECTS_PATH + project_name + "/"
	commands = [
		[
			defaults.P4C_BM_SCRIPT,
			defaults.PROJECT_P4_NAME + project_name + ".p4",
			"--json",
			defaults.PROJECT_BUILD_NAME + project_name + ".json"
		]
	]
	helpers.execute_commands(commands, path)

def build_project(project_name):
	""
	gen_project_json(project_name)

if __name__ == '__main__':

	build_project("direct_flow_counter")