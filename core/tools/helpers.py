#!/usr/bin/env python

import subprocess
import jinja2
import defaults

def execute_commands(commands, cwd, stdin = None):
	""
	for command in commands:
		subprocess.call(command, shell = False, cwd = cwd, stdin = stdin)

def render_template(file, context):
	""
	j2_env = jinja2.Environment(loader = jinja2.FileSystemLoader(defaults.TEMPLATES_PATH))
	return j2_env.get_template(file).render(context)

def write_file(path, content):
	""
	file = open(path, 'w')
	file.write(content)
	file.close()