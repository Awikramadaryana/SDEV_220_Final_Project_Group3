# Inventory Ordering System
# This will receive user input through textboxes and write to a text file

import tkinter as tk
from settingsMenu import default_settings
from tkinter import ttk
from inventory_master import InventoryItem as inv
from inventory_master import default_inventory

class OrderMenu(tk.Tk):
    def __init__(self, screenName = None, baseName = None, className = "Tk", useTk = True, sync = False, use = None):
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.title("Inventory Menu")
        self.geometry("500x500")
        self.stock_items = []
        self.configure(bg=default_settings.background)

        #declare string variables to store item details
        self.nameStr = tk.StringVar()
        self.qtyStr = tk.StringVar()
        
        #creating a list of variables for a dropdown menu
        for i, name in enumerate(default_inventory.cafe_inventory.keys()):
            self.stock_items.append(name)
            print(name)
            
            # prepping options for the drop down menu
        self.selectedOption = tk.StringVar(self)
        self.selectedOption.set(self.stock_items[0])
        
        # leftover from attempt to make a quick inventory menu, decided against it for the sake of getting project completed
        # Todo: Figure out how to make this work alter
        #self.selectedOption.set("Inventory At a Glance")
        self.selectedData = tk.IntVar(self)
        self.selectedIndex = 0

        #Label Declarations
        self.orderLabel = tk.Label(self, text="Create New Order")
        self.nameLabel = tk.Label(self, text = "Enter Item name")
        self.itemQty = tk.Label(self, text="Insert Item Quantity")

        #User Entry Declarations
        self.nameEntry = ttk.Entry(self, textvariable = self.nameStr)
        self.qtyEntry = ttk.Entry(self, textvariable = self.qtyStr)

        #UI elements
        self.orderLabel.pack()

        self.nameLabel.pack()
        tk.OptionMenu(self, self.selectedOption, *self.stock_items).pack()
        #self.nameEntry.pack()

        self.itemQty.pack()
        self.qtyEntry.pack()

        #Submit button
        sub_btn=tk.Button(self,text = 'Submit', command = self.submit)
        sub_btn.pack()
        

    #Function to submit currently held variables into txt file
    def submit(self):
        name = self.nameStr.get()
        qty=self.qtyStr.get()
        
        #Write input to file
        #with open("OrderList.txt", "a") as f:
        #    f.write(item)
        #with open("OrderList.txt", "a") as f:
        #    f.write(qty)
        #with open("OrderList.txt", "a") as f:
        #    f.write(name)
        
        name = self.selectedOption.get()
        
        if name in default_inventory.cafe_inventory:
            item = default_inventory.cafe_inventory[name]
            item.add_stock(int(qty))
        else:
            print(f"Item '{name}' not found in inventory.")
            return

        default_inventory.add_stock(name, int(qty))

        print("The item is : " + name)
        print("The Quantity is : " + qty)
        
        
        self.nameStr.set("")
        self.qtyStr.set("")