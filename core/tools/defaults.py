#!/usr/bin/env python

import os

TOOLS_DIR = os.path.dirname(os.path.abspath(__file__)) + "/"

APP_DIR = TOOLS_DIR + "../../"

PROJECTS_DIR = APP_DIR + "projects/"
CORE_DIR = APP_DIR + "core/"
GIT_MODULES_DIR = APP_DIR + "git_modules/"

TEMPLATES_DIR = CORE_DIR + "templates/"
TOOLS_DIR = CORE_DIR + "tools/"

BMV2_DIR = GIT_MODULES_DIR + "bmv2/"
P4C_BM_DIR = GIT_MODULES_DIR + "p4c-bm/"
FLOODLIGHT_DIR = GIT_MODULES_DIR + "floodlight/"

PROJECT_P4_NAME = "p4/"
PROJECT_UTIL_NAME = "util/"
PROJECT_TOOLS_NAME = "tools/"
PROJECT_MININET_NAME = "mininet/"