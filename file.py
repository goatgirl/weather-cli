import os.path
import json


def exists(file):
    return os.path.exists(file)


def read(file):
    if not exists(file):
        return None
    with open(file, 'r') as f:
        data = f.read()
    return data


def save(file, data):
    with open(file, 'w') as f:
        f.write(str(data))


def save_json(file, data):
    with open(file, 'w') as file:
        file.write(json.dumps(data))

def read_json(file):
    with open(file) as file:    
        return json.load(file)


def rename(old, new):
    os.rename(old, new)
