"""
Name: inventory_master.py
Author: Team 3
Date last updated: 8 Mar 2026
Description:
This file has two classes that allow the creation of our inventory system, one instantiates an inventory itself, the other instantiates each individual inventory item
Each inventory item is allowed to have stock added or removed, while the CafeInventory allows brand new items to be added to said inventory without issue.
"""

# Class that defines what an inventory item is
class InventoryItem:
    def __init__(self, name, full_stock, stock, reorder_level):
        self.name = name
        self.full_stock = full_stock
        self.stock = stock
        self.reorder_level = reorder_level

    # allows stock to be added via the inventory order menu
    def add_stock(self, amount):
        print("Add stock has been called")
        self.stock = self.stock + amount
        print(self.stock)

    # allows stock to be removed from the inventory during inventory checks
    def remove_stock(self, amount):
        if amount <= self.stock:
            self.stock -= amount
        else:
            print("Not enough stock!")

    # Tells when a specific item needs a order to be placed for it
    def needs_reorder(self):
        return self.stock <= self.reorder_level


# Class that manages the cafe inventory
class CafeInventory:
    def __init__(self):
        # SAME name you used before
        self.cafe_inventory = {}
        self.inventoryCount = 0

    # allows users to add a brand new item to the dictionary at any time
    def add_item(self, name, full_stock, stock, reorder_level):
        self.cafe_inventory[name] = InventoryItem(name, full_stock, stock, reorder_level)
        self.inventoryCount += self.inventoryCount

    # Checks item for updating the amount of inventory available, no longer being used
    def update_item(self, name, stock=None, reorder_level=None):
        if name in self.cafe_inventory:
            if stock is not None:
                self.cafe_inventory[name].stock = stock
            if reorder_level is not None:
                self.cafe_inventory[name].reorder_level = reorder_level
        else:
            print("Item not found.")

    # Allows the inventory menu to check whether or not the inventory item needs to get a new order placed
    def check_reorders(self):
        for item in self.cafe_inventory.values():
            if item.needs_reorder():
                print(f"{item.name} needs to be reordered!")
                display_text = (f"{item.name} needs to be reordered!")
                return display_text

    # sends display information for the stock and reorder level to any area
    def display_inventory(self):
        for item in self.cafe_inventory.values():
            print(f"{item.name} - Stock: {item.stock}, Reorder Level: {item.reorder_level}")
            #display_text = (f"{item.name} - Stock: {item.stock}\n, Reorder Level: {item.reorder_level}")
            
            
default_inventory = CafeInventory()
default_inventory.add_item("Coffee Beans", 50, 25, 10)
default_inventory.add_item("Milk", 20, 5, 5)
default_inventory.add_item("Sugar", 30, 20, 8)


# --------- Program Starts Here ---------
"""
inventory = CafeInventory()

inventory.add_item("Coffee Beans", 50, 10)
inventory.add_item("Milk", 20, 5)
inventory.add_item("Sugar", 30, 8)

inventory.display_inventory()


inventory.remove_stock = inventory.cafe_inventory["Coffee Beans"].remove_stock
inventory.remove_stock(45)

inventory.check_reorders()
"""