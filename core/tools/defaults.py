#!/usr/bin/env python

import os

TOOLS_PATH = os.path.dirname(os.path.abspath(__file__)) + "/"

APP_PATH = TOOLS_PATH + "../../"

PROJECTS_PATH = APP_PATH + "projects/"
CORE_PATH = APP_PATH + "core/"
GIT_MODULES_PATH = APP_PATH + "git_modules/"

TEMPLATES_PATH = CORE_PATH + "templates/"
TOOLS_PATH = CORE_PATH + "tools/"

BMV2_PATH = GIT_MODULES_PATH + "bmv2/"
P4C_BM_PATH = GIT_MODULES_PATH + "p4c-bm/"
FLOODLIGHT_PATH = GIT_MODULES_PATH + "floodlight/"

PROJECT_P4_NAME = "p4/"
PROJECT_UTIL_NAME = "util/"
PROJECT_TOOLS_NAME = "tools/"
PROJECT_MININET_NAME = "mininet/"