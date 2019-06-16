# -*- coding:utf-8 -*-
import yaml
from yaml import CLoader as Loader
import os


OUT_DIR = 'ninja.out/'
ROOT_DIR = './'

TOP_DIRS = ['arch']


def find_yaml(top_dir):
    return []


def read_yaml(f_path):
    with open(f_path) as f:
        conf = yaml.load(f.read(), Loader=Loader)

    return conf


def main():
    os.chdir('../..')

    for td in TOP_DIRS:
        yaml_files = find_yaml(td)

        for fp in yaml_files:
            conf = read_yaml(fp)


if __name__ == '__main__':
    main()
