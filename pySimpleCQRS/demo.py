'''
Created on 05/11/2012

@author: rwidelka
'''
from inventory.fakebus import FakeBus 
from inventory.event_store import EventStore
from inventory.domain import Repository, InventoryItem
from inventory.commands import CreateInventoryItem, DeactivateInventoryItem, RenameInventoryItem
from inventory.inventory_command_handlers import InventoryCommandHandler
from inventory.events import InventoryItemCreated, InventoryItemRenamed, InventoryItemDeactivated
from inventory.read_model import InventoryListView, print_list

def main():
    bus = FakeBus()
    event_store = EventStore(bus)
    repository = Repository(event_store, InventoryItem)
    commands = InventoryCommandHandler(repository)
    bus.register_handler(CreateInventoryItem, commands.handle)
    bus.register_handler(DeactivateInventoryItem, commands.handle)
    bus.register_handler(RenameInventoryItem, commands.handle)
    
    list_view = InventoryListView()
    bus.register_handler(InventoryItemCreated, list_view.handle_item_created)
    bus.register_handler(InventoryItemRenamed, list_view.handle_item_renamed)
    bus.register_handler(InventoryItemDeactivated, list_view.handle_item_deactivated)
    
#    print event_store
    bus.send(CreateInventoryItem(1, "Test"))
#    print repository.get_by_id(1)
#    print event_store
#    print_list()
    bus.send(RenameInventoryItem(1, "new name", 0))
#    print repository.get_by_id(1)
#    print_list()
    bus.send(DeactivateInventoryItem(1, 1))
    
#    print repository.get_by_id(1)
#    print event_store

    print_list()
    

if __name__ == '__main__':
    main()