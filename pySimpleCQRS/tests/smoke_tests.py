'''
Created on 02/11/2012

@author: rwidelka
'''
import unittest

from inventory.domain import InventoryItem

class Test(unittest.TestCase):


    def test_create_new_inventory_item(self):
        item = InventoryItem(1, 'Test Item')
        self.assertEqual(item.id, 1)
        self.assertEqual(item.version, 0)
        self.assertEqual(item.activated, True)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()