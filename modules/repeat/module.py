import sys
import random

PRIORITY = 4

def handle(request):
    response = {}
    sentence = request['message'][7:]
    response['message'] = sentence
    return response




INTENTS = [('ripeti(.*)', handle)]