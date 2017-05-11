import os.path


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


def rename(old, new):
    os.rename(old, new)
