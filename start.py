#!/usr/bin/python3

import os
import sys
import threading

#import settings
from settings.general import SETTINGS
from settings.profile import PROFILE

from core.brain import Brain

VERSION = 0.1

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

help = '''help: TODO'''

if len(sys.argv) == 1:
    print (help)

elif sys.argv[1] == 'help':
    print (help)

elif sys.argv[1] == 'version':
    print (str(VERSION))
    
elif sys.argv[1] == 'start':
    logfile = os.path.join(BASE_DIR, SETTINGS['logs_folder'], SETTINGS['logfile'])
    if not os.path.exists(os.path.dirname(logfile)):
        os.makedirs(os.path.dirname(logfile))
        
    brain = Brain(logfile)


    #start interfaces
    interfaces = []
    if sys.version[0:3] == '3.3' or sys.version[0:3] == '3.4':
        from importlib.machinery import SourceFileLoader
        for f in [f for f in os.listdir(os.path.join(BASE_DIR, SETTINGS['io_folder'])) if os.path.isdir(os.path.join(BASE_DIR, SETTINGS['io_folder'], f))]:
            interfaces.append(SourceFileLoader(f, os.path.join(SETTINGS['io_folder'], f, 'io.py')).load_module())
            
    elif sys.version[0:3] == '3.5':
        import importlib.util
        for f in [f for f in os.listdir(os.path.join(BASE_DIR, SETTINGS['io_folder'])) if os.path.isdir(os.path.join(BASE_DIR, SETTINGS['io_folder'], f))]:
            spec = importlib.util.spec_from_file_location(f, os.path.join(SETTINGS['io_folder'], f, 'io.py')).module_from_spec(spec)
            interfaces.append(importlib.util.module_from_spec(spec))
            spec.loader.exec_module(interfaces[-1])
            
    else:
        print ('ERROR: python version not supported')
        
    for i in interfaces:
        i.IO(brain).run()
    
    
else:
    print ('command not supported\n')
    print (help )