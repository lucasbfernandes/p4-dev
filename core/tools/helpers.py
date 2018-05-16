#!/usr/bin/env python

import subprocess
import jinja2
import defaults
import runtime_CLI
from sswitch_CLI import SimpleSwitchAPI

def execute_command(commands, cwd, stdin = None):
	for command in commands:
		subprocess.call(command, shell = False, cwd = cwd, stdin = stdin)

def execute_commands(json,thrift_ip, thrift_port, comandos):
	pre = runtime_CLI.PreType.SimplePreLAG

	services = runtime_CLI.RuntimeAPI.get_thrift_services(pre)
	services.extend(SimpleSwitchAPI.get_thrift_services())

	standard_client, mc_client, sswitch_client = runtime_CLI.thrift_connect(thrift_ip, thrift_port, services)

	runtime_CLI.load_json_config(standard_client, json)

	client = SimpleSwitchAPI(pre, standard_client, mc_client, sswitch_client)

	for comando in comandos:
		if comando.split(" ")[0] == "table_add":
			argumentos = comando.split(" ",1)
			print argumentos[1]
			client.do_table_add(argumentos[1])

def render_template(file, context):
	""
	j2_env = jinja2.Environment(loader = jinja2.FileSystemLoader(defaults.TEMPLATES_PATH))
	return j2_env.get_template(file).render(context)

def write_file(path, content):
	""
	file = open(path, 'w')
	file.write(content)
	file.close()