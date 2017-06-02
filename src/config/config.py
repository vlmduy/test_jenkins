import json
import os

try:
    env = os.environ['PYTHON_ENV']
except KeyError:
    env = 'development'


def load_config():
    with open('src/config/config.json') as data_file:
        data = json.load(data_file)
    data['environemnt'] = env
    return data[env]
