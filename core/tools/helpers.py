#!/usr/bin/env python

import subprocess
import jinja2
import defaults

def execute_commands(commands, cwd):
	""
	for command in commands:
		subprocess.call(command, shell = False, cwd = cwd)

def render_template(file, context):
	""
	j2_env = jinja2.Environment(loader = jinja2.FileSystemLoader(defaults.TEMPLATES_DIR))
	return j2_env.get_template(file).render(context)