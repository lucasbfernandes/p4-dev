# p4-dev

## Description

Workspace for p4 related development.

## Installation

The first step is to clone this project by typing:

    $ git clone https://github.com/lucasbfernandes/p4-dev.git

After it, go to the root of the repository and type:

    $ python core/tools/build.py

This single command will install all dependencies needed by this project. It will probably take a long time, so feel free to grab your coffee and start reading something cool :)
<br>
<br>
You won't need any further installation commands.

## Usage

If you wish to generate a new p4 project, run:

    $ python core/tools/gen_project.py <project-name>

It will generate a new project called \<project-name> inside the projects/ folder. It will come with some default files, such as tools/build_project.py, tools/run_project.py, tools/run_cli.py, tools/apply_commands.py, p4/\<project-name>.p4, mininet/\<project-name>.py, etc. You are free to edit them as you wish, but be careful, you might have to manually set the paths used by some of the configuration files.
<br>
<br>
These are the only things you have to do in order to start building your p4 application. Feel free to check the three examples in this repository. They have their own DOC.md files explaining what they're meant to and how to run them.

## Future work

* Auto generate mininet files for a new project
* Auto generate p4 example program
* Better way to generate files?
* Tests
* Floodlight integration
* P4 16?
