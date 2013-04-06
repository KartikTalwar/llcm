import os
import sys
import subprocess


class LXC:

    def __init__(self, **kwargs):
        self.options = kwargs


    def shell(self, command, stdout=False):
        if stdout:
            return subprocess.check_output(command, shell=True)
        return subprocess.check_call(command, shell=True)


lxc = LXC()
print lxc.shell('ls -l', False)
