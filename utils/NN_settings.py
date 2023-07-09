# imsize = 512 if torch.cuda.is_available() else 128
import configparser
import pathlib
import os
from config.config import CACHE_PATH


def create_def_config(path):
    path = pathlib.Path(CACHE_PATH, str(path))
    if not os.path.exists(path):
        os.makedirs(path)

    path = pathlib.Path(path, 'user_config.ini')
    if not os.path.exists(path):
        config = configparser.ConfigParser()
        config['user'] = {}
        config['user']['imgsize'] = '128'
        config['user']['iterations'] = '300'
        with open(path, 'w') as configfile:
            config.write(configfile)


def change_conf(conf, value, path):
    path = pathlib.Path(path, 'user_config.ini')
    config = configparser.ConfigParser()
    config.read(path)
    config['user'][conf] = str(value)
    with open(path, 'w') as configfile:
        config.write(configfile)


def get_conf(path):
    path = pathlib.Path(path, 'user_config.ini')
    config = configparser.ConfigParser()
    config.read(path)
    return config['user']['imgsize'], config['user']['iterations']
