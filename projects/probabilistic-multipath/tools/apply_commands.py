#!/usr/bin/env python

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../../core/tools/")

import defaults
import helpers

def apply_commands(project_name, source_name, thrift_port, commands_name):
	""
	path = defaults.PROJECTS_PATH + project_name + "/"
	stdin = open(path + defaults.PROJECT_UTIL_NAME + commands_name)
	commands = [
		[
			defaults.BMV2_CLI_PATH,
			defaults.PROJECT_BUILD_NAME + source_name + ".json",
			thrift_port
		]
	]
	helpers.execute_commands(commands, path, stdin)

if __name__ == '__main__':
	print('COMMAND #1 - THRIFT 9090')
	apply_commands('probabilistic-multipath', 'multipath_switch/multipath-switch', '9090', 's1_commands.txt')

	print('\nCOMMAND #2 - THRIFT 9091')
	apply_commands('probabilistic-multipath', 'dummy_switch/dummy-switch', '9091', 's2_commands.txt')

	print('\nCOMMAND #3 - THRIFT 9092')
	apply_commands('probabilistic-multipath', 'dummy_switch/dummy-switch', '9092', 's3_commands.txt')

	print('\nCOMMAND #4 - THRIFT 9093')
	apply_commands('probabilistic-multipath', 'dummy_switch/dummy-switch', '9093', 's4_commands.txt')

	print('\nCOMMAND #5 - THRIFT 9094')
	apply_commands('probabilistic-multipath', 'multipath_switch/multipath-switch', '9094', 's5_commands.txt')
