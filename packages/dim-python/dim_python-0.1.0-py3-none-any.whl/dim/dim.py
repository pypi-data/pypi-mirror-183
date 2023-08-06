import os
import subprocess
import re
import json
import csv
import requests


DIM_FILE_PATH = os.environ.get('DIM_FILE_PATH', './')


def load_data(name, file_type='text', dim_file_path=DIM_FILE_PATH, encoding='utf-8'):
    base_path = dim_file_path.rstrip('/')
    dim_lock_json = load_dim_lock_json(base_path, encoding)
    if 'contents' not in dim_lock_json:
        return None
    for content in dim_lock_json['contents']:
        if content['name'] == name:
            data_path = content['path'].lstrip('./')
            with open(f'{base_path}/{data_path}', encoding=encoding) as f:
                if file_type == 'json':
                    return json.load(f)
                elif file_type == 'csv':
                    return csv.DictReader(f)
                else:
                    return f.read()


def fetch_data(name, dim_file_path=DIM_FILE_PATH):
    base_path = dim_file_path.rstrip('/')
    dim_json = load_dim_json(base_path)
    for content in dim_json['contents']:
        if content['name'] == name:
            return requests.get(content['url'])


def load_dim_json(dim_file_path=DIM_FILE_PATH, encoding='utf-8'):
    base_path = dim_file_path.rstrip('/')
    with open(f'{base_path}/dim.json', encoding=encoding) as f:
        return json.load(f)


def load_dim_lock_json(dim_file_path=DIM_FILE_PATH, encoding='utf-8'):
    base_path = dim_file_path.rstrip('/')
    with open(f'{base_path}/dim-lock.json', encoding=encoding) as f:
        return json.load(f)


def init():
    cmd = ['dim', 'init']
    completed_process = subprocess.run(cmd)
    return completed_process.returncode == 0


def install(source, name, postprocesses=[], force=False, async_install=False):
    cmd = ['dim', 'install']
    if re.match(r'^https?:\/\/', source):
        cmd.append(source)
    else:
        cmd.extend(['-f', source])
    cmd.extend(['-n', name])
    for postprocess in postprocesses:
        cmd.extend(['-p', postprocess])
    if force:
        cmd.append('-F')
    if async_install:
        cmd.append('-A')

    completed_process = subprocess.run(cmd)
    return completed_process.returncode == 0


def uninstall(name):
    cmd = ['dim', 'uninstall', name]
    completed_process = subprocess.run(cmd)
    return completed_process.returncode == 0


def update(name=None, async_insatll=False):
    cmd = ['dim', 'update']
    if name:
        cmd.append(name)
    if async_insatll:
        cmd.append('-A')
    completed_process = subprocess.run(cmd)
    return completed_process.returncode == 0


def list(simple=False):
    cmd = ['dim', 'list']
    if simple:
        cmd.append('-s')
    completed_process = subprocess.run(cmd)
    return completed_process.stdout


def search(keyword, number=10):
    pass
