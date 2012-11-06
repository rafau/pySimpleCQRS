'''
Created on 05/11/2012

@author: rwidelka
'''

import domain
import inventory.commands as commands

class InventoryCommandHandler(object):
    
    def __init__(self, repository):
        self._repository = repository

    def handle(self, command):
        if command.__class__.__name__ == commands.CreateInventoryItem.__name__:
            item = domain.InventoryItem(command.inventory_item_id, command.name)
            self._repository.save(item, -1)
        elif command.__class__.__name__ == commands.DeactivateInventoryItem.__name__:
            item = self._repository.get_by_id(command.inventory_item_id)
            item.deactivate()
            self._repository.save(item, command.original_version)
        elif command.__class__.__name__ == commands.RenameInventoryItem.__name__:
            item = self._repository.get_by_id(command.inventory_item_id)
            item.change_name(command.new_name)
            self._repository.save(item, command.original_version)
        elif command.__class__.__name__ == commands.CheckInItemsToInventory.__name__:
            item = self._repository.get_by_id(commands.inventory_item_id)
            item.checkin(commands.count)
            self._repository.save(item, commands.original_version)
        elif command.__class__.__name__ == commands.RemoveItemsFromInventory.__name__:
            item = self._repository.get_by_id(command.inventory_item_id)
            item.remove(command.count)
            self._repository.save(item, command.original_version)
