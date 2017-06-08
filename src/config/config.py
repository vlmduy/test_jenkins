"""
src/config/config.py: config
Copyright 2017-2018 LinhHo Training.
"""

import json
import os

try:
    env = os.environ['PYTHON_ENV']
except KeyError:
    env = 'development'


def get_project_path():
    """Get real root path of project
    :rtype : String of project path
    """
    root_dir = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
    # Replace the first occurrence from right to left
    root_dir = root_dir[::-1].replace("/src"[::-1], ""[::-1], 1)[::-1]
    return root_dir


def load_config():
    config_path = '{0}{1}'.format(get_project_path(), '/src/config/config.json')
    with open(config_path) as data_file:
        data = json.load(data_file)
    data['environemnt'] = env
    return data[env]
