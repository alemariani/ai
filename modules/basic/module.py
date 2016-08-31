# -*- coding: utf-8 -*-

import datetime
import random

from settings.general import SETTINGS

PRIORITY = 5

def hello(request):
    response = {}
    response['message'] = "Ciao!"
    return response
    
def time(request):
    response = {}
    now = datetime.datetime.now()
    response['message'] = "Sono le " + str(now.hour) + '.' + str(now.minute).zfill(2)
    return response
    
def whoareyou(request):
    response = {}
    name = SETTINGS['ai_name']
    messages = ['Io sono ' + name + '. Piacere', 'Mi chiamo ' + name, 'Il mio nome è ' + name]
    message = random.choice(messages)
    response['message'] = message
    return response
    
   
INTENTS = [
    ('.*ciao', hello),
    ('.*chi sei', whoareyou),
    ('.*come ti chiami', whoareyou),
    ('.*tuo nome', whoareyou),
    ('.*che ore sono', time),
    ('.*che ora [eè]', time),
    (".*d[ai]mmi (l'ora|le ore)", time),
    ]