"""
File Name: inventoryMenu.py
Author: Team 3
Date last updated: 2/23/2026
Purpose: Provide Inventory interaction menu
"""

import tkinter as tk
from cafeInventory import cafe_inventory
from inventory_master import CafeInventory, InventoryItem, inventory

class inventoryMenu(tk.Tk):
    def __init__(self, screenName = None, baseName = None, className = "Tk", useTk = True, sync = False, use = None):
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.title("Inventory Menu")
        self.geometry("500x500")
        self.stock_items = []
        
        for i, name in enumerate(inventory.cafe_inventory.keys()):
            self.stock_items.append(name)
            print(name)

        # prepping options for the drop down menu
        self.selectedOption = tk.StringVar(self)
        #self.selectedOption.set(self.stock_items[0])
        self.selectedOption.set("Inventory At a Glance")
        self.selectedData = tk.IntVar(self)
        self.selectedIndex = 0

        # Actual Menu
        tk.Label(self, text="Welcome to Inventory Management").pack()
        tk.Label(self, text="Pick an Inventory Item").pack()
        tk.OptionMenu(self, self.selectedOption, *self.stock_items, command=self.updateMenu).pack()
        if self.selectedOption == "Inventory at a Flance":
            for i, full_stock in enumerate(inventory.cafe_inventory.keys()):
                print("The quick inventory statement was called")
            self.quick_inventory = tk.Label.config()
        self.output_label = tk.Label(self, text="Item Pending")
        self.output_label.pack()
        #tk.Button(self, text="Show Data for Item").pack()
        # lbl = tk.Label(self, text=)

    def create_widgets(self):
        paddings = {'padx': 5, 'pady': 5}

    # forgot for updateMenu that you can call a command without passing the info from tk.OptionMenu.
    def updateMenu(self, selection):
        print("Tesing updateMenu has been called")
        selected_item = inventory.cafe_inventory[selection]
        print(selected_item)
        self.output_label.config(text=f'You selected: {selection}')

        #Creating formatted output
        output_text = (f"Item: {selected_item.name}\n"
                       f"Full Stock: {selected_item.full_stock}\n"
                       f"Current Stock: {selected_item.stock}\n"
                       f"Reorder Level: {selected_item.reorder_level}\n")
        self.output_label.config(text=output_text)