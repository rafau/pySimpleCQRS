'''
Created on 05/11/2012

@author: rwidelka
'''

class FakeBus(object):
    
    def __init__(self):
        self._routes = {}
        
    def register_handler(self, command, handler):
        if not self._routes.has_key(command.__name__):
            handlers = [] 
            self._routes[command.__name__] = handlers
        else:
            handlers = self._routes[command.__name__]
        handlers.append(handler)
        
    def send(self, command):
        assert len(self._routes.get(command.__class__.__name__, [])) == 1
        self._routes[command.__class__.__name__][0](command)
        
    def publish(self, event):
        for handler in self._routes.get(event.__class__.__name__, []):
            handler(event)
            