#!/usr/bin/env python3

import xml.etree.ElementTree as ET
#from lxml import html
import os, sys

project_path = ".."
os.chdir(project_path)
sys.path.append(project_path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "animegifsweb.settings")

#os.chdir(project_path)
import django
django.setup()