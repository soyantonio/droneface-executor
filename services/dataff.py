# -*- coding: utf-8 -*-

import subprocess

data = {
    "ad34f389": {
        'index': 0,
        'run': 'services/rtest/test00.py'
    },
    "bd3f8c47": {
        'index': 1,
        'run': 'services/rtest/test01.py'
    },
    "0aa433d2": {
        'index': 2,
        'run': 'services/rtest/test02.py'
    },
    "a73cdae8": {
        'index': 3,
        'run': 'services/rtest/test03.py'
    },
}


def is_present(id):
    return id in data


def is_not_present(id):
    return not is_present(id)


def get_index(id):
    return data[id]['index']


def run(id):
    if is_present(id):
        subprocess.Popen(["python", data[id]['run']])
        return 'Running service #' + str(get_index(id))
    else:
        return 'Invalid service'
