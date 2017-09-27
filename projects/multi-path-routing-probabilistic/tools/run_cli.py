#!/usr/bin/env python

import sys
import os
import argparse

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../../core/tools/')

import defaults
import helpers

def run_cli(project_name, source_name, thrift_port):
	path = defaults.PROJECTS_PATH + project_name + '/'
	commands = [
		[
			defaults.BMV2_CLI_PATH,
			defaults.PROJECT_BUILD_NAME + source_name + '.json',
			thrift_port
		]
	]
	helpers.execute_commands(commands, path)

def get_args():
    parser = argparse.ArgumentParser(description='P4 CLI')
    parser.add_argument('--source-name', help='Path to JSON config file', type=str, action='store', required=True)
    parser.add_argument('--thrift-port', help='Thrift server port', type=str, action='store', required=True)
    return parser.parse_args()

if __name__ == '__main__':
	args = get_args()
	run_cli('multi-path-routing', args.source_name, args.thrift_port)