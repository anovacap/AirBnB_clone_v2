#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the
 contents of the web_static"""
from fabric.api import local
from time import strftime
import os


def do_pack():
    """func - no args"""
    now_time = strftime("%Y%M%d%H%M%S")
    try:
        local("mkdir -p versions")
        file = "versions/web_static_{}.tgz".format(now_time)
        local("tar -cvzf {} web_static/".format(file))
        return file
    except:
        return None
