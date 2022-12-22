# -*- coding: utf-8 -*-

import os
import os.path
import shutil
import glob
import zest.releaser.utils

try:
    import ConfigParser as configparser
except ModuleNotFoundError:
    # python3
    import configparser


def copy(context):
    destinations = get_destinations(
        context["name"], read_configuration("~/.pypirc"), "rt.zestreleaser.pypilocal"
    )
    if not destinations:
        return

    cwd = os.getcwd()
    for destination in destinations:
        target = None
        if os.path.isdir(destination) and not destination.startswith("."):
            target = destination
        elif os.path.isdir(os.path.join(cwd, destination)):
            target = os.path.abspath(os.path.join(cwd, destination))

        if not target or not zest.releaser.utils.ask("Copy egg to folder %s" % target):
            continue

        sources = glob.glob(os.path.join(context["tagdir"], "dist", "*"))
        for source in sources:
            shutil.copy(source, target)


def read_configuration(filename):
    config = configparser.ConfigParser()
    config.read(os.path.expanduser(filename))
    return config


def get_destinations(package, config, section):
    destinations = []
    if section not in config.sections():
        return destinations
    for prefix, path in config.items(section):
        destinations.append(path)
    return destinations
