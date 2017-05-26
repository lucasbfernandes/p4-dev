#!/usr/bin/env python

import defaults
import helpers

def install_dependencies():
	""
	commands = [
		["sudo", "apt-get", "install", "-y", "build-essential", "ant", "maven", "python-dev", "mininet"],
		["sudo", "pip", "install", "Jinja2"]
	]
	helpers.execute_commands(commands, defaults.APP_PATH)

def initialize_modules():
	""
	commands = [
		["git", "submodule", "update", "--init", "--recursive"]
	]
	helpers.execute_commands(commands, defaults.APP_PATH)

def install_bmv2():
	""
	commands = [
		["bash", "install_deps.sh"],
		["bash", "autogen.sh"],
		["bash", "configure"],
		["make"],
		["sudo", "make", "install"]
	]
	helpers.execute_commands(commands, defaults.BMV2_PATH)

def install_p4cbm():
	""
	commands = [
		["sudo", "pip", "install", "-r", "requirements.txt"],
		["sudo", "python", "setup.py", "install"],
	]
	helpers.execute_commands(commands, defaults.P4C_BM_PATH)

def install_floodlight():
	""
	commands = [
		["git", "submodule", "init"],
		["git", "submodule", "update"],
		["ant"],
		["sudo", "mkdir", "/var/lib/floodlight"],
		["sudo", "chmod", "777", "/var/lib/floodlight"],
	]
	helpers.execute_commands(commands, defaults.FLOODLIGHT_PATH)

def install_modules():
	""
	initialize_modules()
	install_bmv2()
	install_p4cbm()
	install_floodlight()

if __name__ == '__main__':

	install_dependencies()
	install_modules()