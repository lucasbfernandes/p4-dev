#!/usr/bin/env python

import subprocess
import defaults

def execute_commands(commands, cwd):
	""
	for command in commands:
		subprocess.call(command, shell = False, cwd = cwd)

def install_dependencies():
	""
	commands = [
		["sudo", "apt-get", "install", "-y", "build-essential", "ant", "maven", "python-dev"]
	]
	execute_commands(commands)

def initialize_modules():
	""
	commands = [
		["git", "submodule", "update", "--init", "--recursive"]
	]
	execute_commands(commands)

def install_bmv2():
	""
	commands = [
		["cd", defaults.BMV2_DIR],
		["bash", "install_deps.sh"],
		["bash", "autogen.sh"],
		["bash", "configure"],
		["make"],
		["sudo", "make", "install"],
		["cd", defaults.BASE_DIR]
	]
	execute_commands(commands)

def install_p4cbm():
	""
	commands = [
		["cd", defaults.P4C_BM_DIR],
		["sudo", "pip", "install", "-r", "requirements.txt"],
		["sudo", "python", "setup.py", "install"],
		["cd", defaults.BASE_DIR]
	]
	execute_commands(commands)

def install_floodlight():
	""
	commands = [
		["cd", defaults.FLOODLIGHT_DIR],
		["git", "submodule", "init"],
		["git", "submodule", "update"],
		["ant"],
		["sudo", "mkdir", "/var/lib/floodlight"],
		["sudo", "chmod", "777", "/var/lib/floodlight"],
		["cd", defaults.BASE_DIR]
	]
	execute_commands(commands)

def install_modules():
	""
	initialize_modules()
	install_bmv2()
	install_p4cbm()
	install_floodlight()

install_dependencies()
install_modules()
