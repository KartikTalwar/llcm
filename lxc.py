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


    def create(self, node, **kwargs):
        cmd = "lxc-create -n %s" % (node)
        return self.shell(cmd)


    def destroy(self, node, **kwargs):
        cmd = "lxc-destroy -n %s" % (node)
        return self.shell(cmd)


