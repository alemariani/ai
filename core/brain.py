import os
import sys
import re
from enum import Enum
import datetime

from settings.general import SETTINGS

class Brain:

    class LogLevel(Enum):
        INFO = 1
        WARNING = 2
        ERROR = 3
    
    def __init__(self, logfile):
        self.modules = []
        self.intents = []
        self.logfp = open(logfile, 'a')
        
        if sys.version[0:3] == '3.3' or sys.version[0:3] == '3.4':
            from importlib.machinery import SourceFileLoader
            for f in [f for f in os.listdir(os.path.join(SETTINGS['modules_folder'])) if os.path.isdir(os.path.join(SETTINGS['modules_folder'], f))]:
                self.modules.append(SourceFileLoader(f, os.path.join(SETTINGS['modules_folder'], f, 'module.py')).load_module())
                
        elif sys.version[0:3] == '3.5':
            import importlib.util
            for f in [f for f in os.listdir(os.path.join(SETTINGS['modules_folder'])) if os.path.isdir(os.path.join(SETTINGS['modules_folder'], f))]:
                spec = importlib.util.spec_from_file_location(f, os.path.join(SETTINGS['modules_folder'], f, 'module.py')).module_from_spec(spec)
                self.modules.append(importlib.util.module_from_spec(spec))
                spec.loader.exec_module(self.modules[-1])
                
        else:
            print ('ERROR: python version not supported')
            
        for m in self.modules:
            for i in m.INTENTS:
                self.intents.append((m.PRIORITY, re.compile(i[0], re.I), i[1]))
        self.intents.sort(reverse=True, key=lambda x: x[0])
        
    def __call__(self, request):
        try:
            self.log(self.LogLevel.INFO, 'Request ' + str(request))
            for i in self.intents:
                if i[1].match(request['message']) is not None:
                    response = i[2](request)
                    self.log(self.LogLevel.INFO, 'Response ' + str(response))
                    return response
        except Exception:
            self.log(self.LogLevel.ERROR, 'An error occurred')
            response = {}
            sponse['message'] = 'An error occurred'
            return response
                
        self.log(self.LogLevel.WARNING, 'Response: No intents found')
        response = {}
        response['message'] = 'No intents found'
        return response
                
                
    def log(self, loglevel, message):
        timestamp = str(datetime.datetime.now())[0:-7]
        self.logfp.write('[' + loglevel.name + ' ' + timestamp + '] ' + message + '\n')