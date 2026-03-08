# Inventory Ordering System
# This will receive user input through textboxes and write to a text file
# A drop down menu has been added to select current items in inventory

import tkinter as tk
from settingsMenu import default_settings
from tkinter import ttk
from inventory_master import InventoryItem as inv
from inventory_master import default_inventory

#Construct new class OrderMenu to be called via main menu
class OrderMenu(tk.Tk):
    def __init__(self, screenName = None, baseName = None, className = "Tk", useTk = True, sync = False, use = None):
        #Initialize main UI
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.title("Inventory Menu")
        self.geometry("500x500")
        self.stock_items = []
        self.configure(bg=default_settings.background)

        #declare string variables to store item details
        self.nameStr = tk.StringVar(self)
        self.qtyVar = tk.StringVar(self)
        
        #creating a list of variables for a dropdown menu
        for i, name in enumerate(default_inventory.cafe_inventory.keys()):
            self.stock_items.append(name)
            print(name)
            
        # prepping options for the drop down menu
        self.selectedOption = tk.StringVar(self)
        self.selectedOption.set(self.stock_items[0])
        self.selectedData = tk.IntVar(self)
        self.selectedIndex = 0

        #Label Declarations
        self.orderLabel = tk.Label(self, text="Create New Order")
        self.nameLabel = tk.Label(self, text = "Enter Item name")
        self.itemQty = tk.Label(self, text="Insert Item Quantity")

        #User Entry Declarations
        self.nameEntry = ttk.Entry(self, textvariable = self.nameStr)
        self.qtyEntry = ttk.Entry(self, textvariable = self.qtyVar)

        #Load in Labels and Buttons
        self.orderLabel.pack()

        self.nameLabel.pack()
        tk.OptionMenu(self, self.selectedOption, *self.stock_items).pack()

        self.itemQty.pack()
        self.qtyEntry.pack()

        #Submit button
        sub_btn=tk.Button(self,text = 'Submit', command = self.submit)
        sub_btn.pack()
        

    #Function to submit currently held variables into dictionary
    def submit(self):
        qty=self.qtyVar.get()
        name = self.selectedOption.get()
        
        if name in default_inventory.cafe_inventory:
            item = default_inventory.cafe_inventory[name]
            item.add_stock(int(qty))
        else:
            print(f"Item '{name}' not found in inventory.")
            return

        #print check
        print("The item is : " + name)
        print("The item quantity is : " + qty)
        
        
        self.nameStr.set("")
        self.qtyVar.set("")