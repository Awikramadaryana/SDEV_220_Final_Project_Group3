# Class that defines what an inventory item is
class InventoryItem:
    def __init__(self, name, stock, reorder_level):
        self.name = name
        self.stock = stock
        self.reorder_level = reorder_level

    def add_stock(self, amount):
        self.stock += amount

    def remove_stock(self, amount):
        if amount <= self.stock:
            self.stock -= amount
        else:
            print("Not enough stock!")

    def needs_reorder(self):
        return self.stock <= self.reorder_level


# Class that manages the cafe inventory
class CafeInventory:
    def __init__(self):
        # SAME name you used before
        self.cafe_inventory = {}

    def add_item(self, name, stock, reorder_level):
        self.cafe_inventory[name] = InventoryItem(name, stock, reorder_level)

    def update_item(self, name, stock=None, reorder_level=None):
        if name in self.cafe_inventory:
            if stock is not None:
                self.cafe_inventory[name].stock = stock
            if reorder_level is not None:
                self.cafe_inventory[name].reorder_level = reorder_level
        else:
            print("Item not found.")

    def check_reorders(self):
        for item in self.cafe_inventory.values():
            if item.needs_reorder():
                print(f"{item.name} needs to be reordered!")

    def display_inventory(self):
        for item in self.cafe_inventory.values():
            print(f"{item.name} - Stock: {item.stock}, Reorder Level: {item.reorder_level}")


# --------- Program Starts Here ---------

inventory = CafeInventory()

inventory.add_item("Coffee Beans", 50, 10)
inventory.add_item("Milk", 20, 5)
inventory.add_item("Sugar", 30, 8)

inventory.display_inventory()

inventory.remove_stock = inventory.cafe_inventory["Coffee Beans"].remove_stock
inventory.remove_stock(45)

inventory.check_reorders()