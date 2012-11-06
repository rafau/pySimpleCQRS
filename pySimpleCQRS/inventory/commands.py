'''
Created on 02/11/2012

@author: rwidelka
'''
class CreateInventoryItem(object):
    
    def __init__(self, inventory_item_id, name):
        self.inventory_item_id = inventory_item_id
        self.name = name

class DeactivateInventoryItem(object):
    
    def __init__(self, inventory_item_id, original_version):
        self.inventory_item_id = inventory_item_id
        self.original_version = original_version

class RenameInventoryItem(object):
    
    def __init__(self, inventory_item_id, new_name, original_version):
        self.inventory_item_id = inventory_item_id
        self.original_version = original_version
        self.new_name = new_name

class CheckInItemsToInventory(object):
    
    def __init__(self, inventory_item_id, count, original_version):
        self.inventory_item_id = inventory_item_id
        self.original_version = original_version
        self.count = count

class RemoveItemsFromInventory(object):
    
    def __init__(self, inventory_item_id, count, original_version):
        self.inventory_item_id = inventory_item_id
        self.original_version = original_version
        self.count = count
