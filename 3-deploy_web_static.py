#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to
my web servers
"""

import os
from fabric.api import *
from datetime import datetime


env.hosts = ['54.237.97.154', '54.224.31.23']



def deploy():
    """
    Creates and distributes an archive
    """
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)


def do_pack():
    """
    Pack web_static content
    """
    local("mkdir -p versions")
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y%m%d%H%M%S")
    path = "versions/web_static_" + formatted_datetime + ".tgz"
    cmd = "tar -cvzf {} web_static".format(path)

    if local(cmd).failed:
        return None
    return path


def do_deploy(archive_path):
    """
    Distributes archive to the web servers
    Arg:
        archive_path (file)
    """
    if not os.path.exists(archive_path):
        return False

    path = "/data/web_static/releases/"
    name = archive_path.split("/")[1]
    no_exten = name.split(".")[0]

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
