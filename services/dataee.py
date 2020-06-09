# -*- coding: utf-8 -*-
# import time
# import os
# import signal
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


class TestClass():
    def test_f(self, name):
        subprocess.call("python services/rtest/test00.py", shell=True)


def run(id):
    if is_present(id):
        command = ["python", data[id]['run']]
        subprocess.Popen(command)

        # time.sleep(1)
        # os.kill(os.getpgid(proc.pid), signal.SIGTERM)
        # os.kill(proc.pid, signal.SIGTERM)
        # proc.terminate()
        # try:
        #     outs, _ = proc.communicate(timeout=0.2)
        #     print('== subprocess exited with rc =', proc.returncode)
        #     print(outs)
        # except subprocess.TimeoutExpired:
        #     print('subprocess did not terminate in time')
        # subprocess.Popen(command)
        # time.sleep(1)
        # process.terminate()
        # pro.terminate()
        # subprocess.Popen("TASKKILL /F /PID {pid} /T".format(pid=process.pid))
        # pro.kill()
        # os.killpg(os.getpgid(pro.pid), signal.SIGTERM)
        return 'Running service #' + str(get_index(id))
    else:
        return 'Invalid service'
