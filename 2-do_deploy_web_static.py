#!/usr/bin/python3
"""
Fabric script that distributes an archive to
your web serversusing do_deploy function
"""

import os
from fabric.api import *


env.hosts = ['54.237.97.154', '54.224.31.23']


def do_deploy(archive_path):
    """
    Distributes archive to the web servers
    Arg:
        archive_path (file)
    """
    if os.path.exists(archive_path) is False:
        return False

    path = "/data/web_static/releases/"
    name = archive_path.split("/")[-1]
    no_exten = name.rsplit(".", 1)[0]

    if put(archive_path, "/tmp/").failed:
        return False
    if run("mkdir -p {}{}/".format(path, no_exten)).failed:
        return False
    if run("tar -xzf /tmp/{} -C {}{}/".format(name, path, no_exten)).failed:
        return False
    if run("rm /tmp/{}".format(name)).failed:
        return False
    if run("mv {0}{1}/web_static/* {0}{1}/".format(path, no_exten)).failed:
        return False
    if run("rm -rf {}{}/web_static".format(path, no_exten)).failed:
        return False
    if run("rm -rf /data/web_static/current").failed:
        return False
    if run("ln -s {}{}/ /data/web_static/current".
            format(path, no_exten)).failed:
        return False
    return True
