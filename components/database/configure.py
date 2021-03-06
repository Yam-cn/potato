#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 17:48:19 2016
@author: chopchopjames
"""

from configparser import ConfigParser, NoSectionError, NoOptionError
import os

def getConfigInfo(key):
    parser = ConfigParser()
    parser.read(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config.ini'))

    serv_conf = {}
    try:
        serv_conf['host'] = parser.get(key, 'host')
        serv_conf['port'] = parser.getint(key, 'port')
        if key == 'Mongo':
            serv_conf['dbname'] = parser.get(key, 'dbname')
    except (NoSectionError, NoOptionError) as err:
        raise Exception('configuration error {0}'.format(err))
        exit(-1)
    return serv_conf


if __name__ == '__main__':
    ret = getConfigInfo('Mongo')
    print ret
