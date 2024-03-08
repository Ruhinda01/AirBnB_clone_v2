#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from contents
if the web_static
"""

from fabric.api import *
from datetime import datetime


def do_pack():
    """
    Pack web_static content
    """
    local("mkdir -p versions") 
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y%m%d%H%M%S")
    path = "versions/web_static_" + formatted_datetime + ".tgz"
    cmd = "tar -cvzf {} web_static".format(path)

    if local(cmd):
        return path
    return None
