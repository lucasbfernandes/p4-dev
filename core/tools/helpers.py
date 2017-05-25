#!/usr/bin/env python

import subprocess

def execute_commands(commands, cwd):
	""
	for command in commands:
		subprocess.call(command, shell = False, cwd = cwd)