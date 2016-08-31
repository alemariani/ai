import sys
import random

PRIORITY = 0

def handle(request):
    response = {}
    messages = ['Non ho capito', 'Non conosco questo comando']
    message = random.choice(messages)
    response['message'] = message
    return response




INTENTS = [('', handle)]