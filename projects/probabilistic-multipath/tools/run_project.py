#!/usr/bin/env python

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../../core/tools/")

import defaults
import helpers

def run_mininet(project_name):
	path = defaults.PROJECTS_PATH + project_name + "/"
	commands = [
		[
			"sudo", "python",
			defaults.PROJECT_MININET_NAME + project_name + ".py",
			"--behavioral-exe",
			defaults.BMV2_INTERPRETER_PATH,
			"--json",
			defaults.PROJECT_BUILD_NAME + project_name + ".json"
		]
	]
	helpers.execute_commands(commands, path)

def run_project(project_name):
	run_mininet(project_name)

if __name__ == '__main__':
	run_project("probabilistic-multipath")