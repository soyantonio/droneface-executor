# -*- coding: utf-8 -*-
import os
import signal
import subprocess


data = {
    "ad34f389": {
        'index': 0,
        'run': 'services/rdrone/drone00.py'
    },
    "bd3f8c47": {
        'index': 1,
        'run': 'services/rdrone/drone01.py'
    },
    "0aa433d2": {
        'index': 2,
        'run': 'services/rdrone/drone02.py'
    },
    "a73cdae8": {
        'index': 3,
        'run': 'services/rdrone/drone03.py'
    },
    "stop": {
        'index': 4,
        'run': '.'
    },
}


def is_present(id):
    return id in data


def is_not_present(id):
    return not is_present(id)


def get_index(id):
    return data[id]['index']


class Executor:
    def __init__(self):
        self.pid = None

    def run(self, id):
        if is_present(id):
            if id == "stop":
                self.stop()
                return "Stopped"

            command = ["python", data[id]['run']]
            proc = subprocess.Popen(command)
            self.pid = proc.pid
            return 'Running service #' + str(get_index(id))
        else:
            return 'Invalid service'

    def stop(self):
        print(self.pid)
        if self.pid is not None:
            print("Stopping")
            os.kill(self.pid, signal.SIGTERM)
            self.pid = None
