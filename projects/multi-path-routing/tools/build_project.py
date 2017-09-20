#!/usr/bin/env python

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../../core/tools/")

import defaults
import helpers

def gen_project_json(project_folder, source_name):
	""
	path = defaults.PROJECTS_PATH + project_folder + "/"
	commands = [
		[
			defaults.P4C_BM_SCRIPT,
			defaults.PROJECT_P4_NAME + source_name + ".p4",
			"--json",
			defaults.PROJECT_BUILD_NAME + source_name + ".json"
		]
	]
	helpers.execute_commands(commands, path)

def build_project(project_folder, source_name):
	""
	gen_project_json(project_folder, source_name)

if __name__ == '__main__':

	print('BUILD #1 - THRIFT 9090 AND 9093')
	build_project('multi-path-routing', 'external_switch/external-switch')
	print('\nBUILD #2 - THRIFT 9091 AND 9092')
	build_project('multi-path-routing', 'inner_switch/inner-switch')