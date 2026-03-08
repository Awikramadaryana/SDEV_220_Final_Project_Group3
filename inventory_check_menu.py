"""
File Name: inventory_check_menu.py
Author: Team 3
Date last updated: 2/23/2026
Purpose: Provide Inventory interaction menu that allows end users to be able to track the inventory minimum stock, the maximum stock, and the current stock available so that orders
can be placed properly.
"""

import tkinter as tk
from cafeInventory import cafe_inventory
from inventory_master import CafeInventory, InventoryItem, default_inventory
from settingsMenu import default_settings

class inventoryMenu(tk.Tk):
    # initialization of the menu
    def __init__(self, screenName = None, baseName = None, className = "Tk", useTk = True, sync = False, use = None):
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.title("Inventory Menu")
        self.geometry("500x500")
        self.stock_items = []
        self.configure(bg=default_settings.background)
        
        # this allows us to create a list of all the names of the items in the dictionary in preparation for using them in a dropdown menu box
        for i, name in enumerate(default_inventory.cafe_inventory.keys()):
            self.stock_items.append(name)
            print(name)

        # prepping options for the drop down menu
        self.selectedOption = tk.StringVar(self)
        self.selectedOption.set(self.stock_items[0])
        
        # leftover from attempt to make a quick inventory menu, decided against it for the sake of getting project completed
        # Todo: Figure out how to make this work alter
        # self.selectedOption.set("Inventory At a Glance")
        self.selectedData = tk.IntVar(self)
        self.selectedIndex = 0

        # Actual Menu
        tk.Label(self, text="Welcome to Inventory Management").pack()
        tk.Label(self, text="Pick an Inventory Item").pack()
        # This creates the actual dropdown menu
        tk.OptionMenu(self, self.selectedOption, *self.stock_items, command=self.updateMenu).pack()
        # Inventory at a Glance was created to make a quick inventory check for items that needed to be reordered. However, because of how long it took to create inventory_master, this feature was cut for time
        """
        if self.selectedOption == "Inventory at a Glance":
            for i, full_stock in enumerate(default_inventory.cafe_inventory.keys()):
                print("The quick inventory statement was called")
            self.quick_inventory = tk.Label.config()
        """
        self.output_label = tk.Label(self, text="Item Pending")
        self.output_label.pack()
        # tk.Button(self, text="Show Data for Item").pack()
        # lbl = tk.Label(self, text=) 
        
        # creating formatted output labels
        self.item_label = tk.Label(self)
        self.full_stock_label = tk.Label(self)
        self.current_stock_label = tk.Label(self)
        self.reorder_level_label = tk.Label(self)

    def create_widgets(self):
        paddings = {'padx': 5, 'pady': 5}

    # forgot for updateMenu that you can call a command without passings the info from tk.OptionMenu.
    def updateMenu(self, selection):
        color = "black"
        print("Tesing updateMenu has been called")
        selected_item = default_inventory.cafe_inventory[selection]
        print(selected_item)
        self.output_label.config(text=f'You selected: {selection}')
        need_to_order = False
        if selected_item.stock <= selected_item.reorder_level:
            color = "red"

        #Creating formatted output
        # this snippet was originally part of the quick menu, but was also cut for time
        """
        Previous version of output code
        output_text = (f"Item: {selected_item.name}\n"
                       f"Full Stock: {selected_item.full_stock}\n"
                       f"Current Stock: {selected_item.stock}\n"
                       f"Reorder Level: {selected_item.reorder_level}\n")
        self.output_label.config(text=output_text)
        """
        self.item_label.config(text=f"Item Name: {selected_item.name}")
        self.full_stock_label.config(text=f"Full Stock: {selected_item.full_stock}")
        self.current_stock_label.config(text=f"Current Stock: {selected_item.stock}", fg=color)
        self.reorder_level_label.config(text=f"Reorder Level: {selected_item.reorder_level}")
        
        # making formatted output appear
        self.item_label.pack()
        self.full_stock_label.pack()
        self.current_stock_label.pack()
        self.reorder_level_label.pack()