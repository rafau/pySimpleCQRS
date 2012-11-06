'''
Created on 05/11/2012

@author: rwidelka
'''

class InventoryItemDetailsDto(object):
    
    def __init__(self, id, name, current_count, version):
        self.id = id
        self.name = name
        self.current_count = current_count
        self.version = version
        
class InventoryItemListDto(object):
    
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
    def __repr__(self):
        return "(%d)%s"%(self.id, self.name)

item_list = []
        
class InventoryListView(object):
    
    def handle_item_created(self, event):
        item_list.append(InventoryItemListDto(event.id, event.name))
        
    def handle_item_renamed(self, event):
        item = filter(lambda e: e.id == event.id, item_list)[0]
        item.name = event.new_name
        
    def handle_item_deactivated(self, event):
        item = filter(lambda e: e.id == event.id, item_list)[0]
        item_list.remove(item)
        
        
def print_list():
    print item_list