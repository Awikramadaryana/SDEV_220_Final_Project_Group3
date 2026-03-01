class CafeInventory:
    def __init__(self):
        self.cafe_inventory = {}

    def add_item(self, name, stock, reorder_level):
        self.cafe_inventory[name] = {
            "stock": stock,
            "reorder_level": reorder_level
        }

    def update_item(self, name, stock=None, reorder_level=None):
        if name in self.cafe_inventory:
            if stock is not None:
                self.cafe_inventory[name]["stock"] = stock
            if reorder_level is not None:
                self.cafe_inventory[name]["reorder_level"] = reorder_level
        else:
            print("Item not found.")

    def remove_stock(self, name, amount):
        if name in self.cafe_inventory:
            if amount <= self.cafe_inventory[name]["stock"]:
                self.cafe_inventory[name]["stock"] -= amount
            else:
                print("Not enough stock!")
        else:
            print("Item not found.")

    def check_reorders(self):
        for name, details in self.cafe_inventory.items():
            if details["stock"] <= details["reorder_level"]:
                print(f"{name} needs to be reordered!")

    def display_inventory(self):
        for name, details in self.cafe_inventory.items():
            print(f"{name} - Stock: {details['stock']}, Reorder Level: {details['reorder_level']}")


inventory = CafeInventory()

inventory.add_item("Coffee Beans", 50, 10)
inventory.add_item("Milk", 20, 5)
inventory.add_item("Sugar", 30, 8)

inventory.display_inventory()

inventory.remove_stock("Coffee Beans", 45)

inventory.check_reorders()