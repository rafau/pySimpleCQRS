'''
Created on 02/11/2012

@author: rwidelka
'''

import inventory.events as events


class AgreateRoot(object):
    
    def __init__(self):
        self._changes = []
        self.version = 0
        self.id = 0
        
    def get_uncommited_changes(self):
        return self._changes
    
    def mark_changes_as_commited(self):
        self._changes = []
        
    def loads_from_history(self, history):
        for e in history:
            self.apply_change(e, False)
    
    def apply_change(self, event, is_new = True):
        self.apply(event)
        if is_new:
            self._changes.append(event)

class Repository(object):
    
    def __init__(self, storage, T):
        self._storage = storage
        self._T = T
        
    def save(self, aggregate, expected_version):
        self._storage.save_events(aggregate.id, aggregate.get_uncommited_changes(), expected_version)
        
    def get_by_id(self, id):
        obj = self._T()
        events = self._storage.get_events_for_aggregate(id)
        obj.loads_from_history(events)
        return obj

class InventoryItem(AgreateRoot):
    
    def __init__(self, id = None, name = None):
        super(InventoryItem, self).__init__()
        self.id = id
        self.activated = False
        if id != None:
            self.apply_change(events.InventoryItemCreated(id, name))
        
    def apply(self, event):
        if event.__class__.__name__ == events.InventoryItemCreated.__name__:
            self.id = event.id
            self.activated = True
        elif event.__class__.__name__ == events.InventoryItemDeactivated.__name__:
            self.activated = False
            
    def change_name(self, new_name):
        self.apply_change(events.InventoryItemRenamed(self.id, new_name))
        
    def remove(self, count):
        self.apply_change(events.ItemsRemovedFromInventory(self.id, count))
        
    def check_in(self, count):
        self.apply_change(events.ItemsCheckedInToInventory(self.id, count))
        
    def deactivate(self):
        self.apply_change(events.InventoryItemDeactivated(self.id))
        
    def __str__(self):
        return "[%s][%s][%s]%s"%(self.id, self.version, self.activated, self.get_uncommited_changes())