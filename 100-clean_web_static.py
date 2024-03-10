#!/usr/bin/python3
"""
Fabric script (based on the file 3-deploy_web_static.py)
that deletes out-of-date archives, using the function do_clean
"""

import os
from fabric.api import *

env.hosts = ['54.237.97.154', '54.224.31.23']


def do_clean(number=0):
    """
    Deletes out_of_date archives
    Args:
        number (int): number of archives to keep
    """
    number = 1 if int(number) == 0 else int(number)

    # sorts outh the archives in the version directory
    archives = sorted(os.listdir("versions"))
    #  creates a list from removal of archives with a loop
    [archives.pop() for x in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
