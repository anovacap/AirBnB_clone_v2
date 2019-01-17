#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the
 contents of the web_static"""
from fabric.api import run, env, put
import os.path
env.hosts = "35.237.167.147, 34.73.249.164"
env.user = "ubuntu"


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


def do_deploy(archive_name):
    """func - arg = archive_name"""
    if os.path.isfile(archive_name) is False:
        return False
    arch_name = archive_name.split("/")[-1]
    try:
        put(archive_name, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}".format(arch_name))
        run("tar -xzf /tmp{} -C /data/web_static/releases{}".format(arch_name,
                                                                    arch_name))
        run("rm /tmp/{}".format(arch_name))
        run("mv /data/web_static/releases/{}/web_static/*\/data/web_static"
            "/releases/{}".format(arch_name, arch_name))
        run("rm -rf /data/web_static/releases/{}/web_static".format(arch_name))
        run("rm -rf /data/web_static/current")
        run("ln -sf /data/web_static/releases/{}/ /data/web_static"
            "/current".format(arch_name))
        print("New version deployed")
        return True
    except BaseException:
        return False
