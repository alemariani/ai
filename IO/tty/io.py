import core.IO

from settings.profile import PROFILE
from settings.general import SETTINGS

class IO (core.IO.IO):
    def __init__(self, brain):
        core.IO.IO.__init__(self, brain)
    
    def run(self):
        while True:
            print (PROFILE['first_name'] + '> ', end='')
            message = input();
            request = {}
            request['message'] = message;
            response = self.brain(request)
            print (SETTINGS['ai_name'] + '> ' + response['message'])