'''
Created on 02/11/2012

@author: rwidelka
'''

class Event(object):
    
    def __init__(self):
        self.version = 0
        
class InventoryItemDeactivated(Event):
    
    def __init__(self, id):
        super(InventoryItemDeactivated, self).__init__()
        self.id = id
        
    def __repr__(self):
        return "ItemDeactivated[%d]"%(self.id)
        
class InventoryItemCreated(Event):
    
    def __init__(self, id, name):
        super(InventoryItemCreated, self).__init__()
        self.id = id
        self.name = name

    def __repr__(self):
        return "ItemCreated[%d][%s]"%(self.id, self.name)
        
class InventoryItemRenamed(Event):
    
    def __init__(self, id, new_name):
        super(InventoryItemRenamed, self).__init__()
        self.id = id
        self.new_name = new_name
        
class ItemsCheckedInToInventory(Event):
    
    def __init__(self, id, count):
        super(ItemsCheckedInToInventory, self).__init__()
        self.id = id
        self.count = count
        
class ItemsRemovedFromInventory(Event):
    
    def __init__(self, id, count):
        super(ItemsRemovedFromInventory, self).__init__()
        self.id = id
        self.count = count
        
