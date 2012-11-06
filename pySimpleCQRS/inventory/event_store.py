'''
Created on 05/11/2012

@author: rwidelka
'''


class ConcurrencyException(Exception):
    pass


class EventDescriptor(object):
    
    def __init__(self, id, event_data, version):
        self.id = id
        self.event_data = event_data
        self.version = version
        
    def __repr__(self):
        return "(%d)[%d]%s"%(self.id, self.version, self.event_data)
        
class EventStore(object):
    
    def __init__(self, event_publisher):
        self._publisher = event_publisher
        self._current = {}
        
    def save_events(self, aggregate_id, events, expected_version):
        if not self._current.has_key(aggregate_id):
            self._current[aggregate_id] = []
        elif self._current[aggregate_id][-1].version != expected_version and expected_version != -1:
            raise ConcurrencyException()
        i = expected_version
        for event in events:
            i += 1
            event.version = i
            self._current[aggregate_id].append(EventDescriptor(aggregate_id, event, i))
            self._publisher.publish(event)
            
    def get_events_for_aggregate(self, aggreagate_id):
        event_descriptors = self._current[aggreagate_id]
        return [ed.event_data for ed in event_descriptors]
    
    def __str__(self):
        return str(self._current)