class Inventory:

    def __init__(self):
        self.inventory = {}

    def add_item(self, name, category, stock, reorder_level,
                 price=None, unit=None, supplier=None,
                 boxed=False, items_per_box=None):

        self.inventory[name] = {
            "category": category,
            "stock": stock,
            "reorder_level": reorder_level,
            "price": price,
            "unit": unit,
            "supplier": supplier,
            "boxed": boxed,
            "items_per_box": items_per_box
        }

    def update_item(self, name, key, value):
        if name in self.inventory:
            self.inventory[name][key] = value
            print("Item updated successfully.")
        else:
            print("Item not found.")

    def add_stock(self, name, amount):
        if name in self.inventory:
            self.inventory[name]["stock"] += amount

    def remove_stock(self, name, amount):
        if name in self.inventory:
            if amount <= self.inventory[name]["stock"]:
                self.inventory[name]["stock"] -= amount
            else:
                print("Not enough stock.")

    def check_reorder(self):
        for name, item in self.inventory.items():
            if item["stock"] <= item["reorder_level"]:
                print(name, "needs reorder.")

    def show_inventory(self):
        for name, item in self.inventory.items():
            print(name, "-", item["stock"])