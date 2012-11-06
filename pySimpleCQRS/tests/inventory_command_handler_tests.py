'''
Created on 05/11/2012

@author: rwidelka
'''
import unittest

from inventory.inventory_command_handlers import InventoryCommandHandler
import inventory.commands as commands
import inventory.events as events

class FakeRepository(object):
    
    def __init__(self):
        self.storage = []
    
    def save(self, aggregate, expected_version):
        self.storage.append(aggregate)

class Test(unittest.TestCase):


    def setUp(self):
        self._repository = FakeRepository()


    def tearDown(self):
        pass


    def test_create_inventory_item(self):
        cmd_handler = InventoryCommandHandler(self._repository)
        cmd = commands.CreateInventoryItem(1, "Test item")
        cmd_handler.handle(cmd)
        self.assertEqual(len(self._repository.storage), 1)
        item = self._repository.storage[0]
        self.assertEqual(item.id, 1)
        self.assertEqual(len(item.get_uncommited_changes()), 1)
        event = item.get_uncommited_changes()[0]
        self.assertEqual(len(item.get_uncommited_changes()), 1)
        self.assertEqual(event.__class__.__name__, events.InventoryItemCreated.__name__)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()