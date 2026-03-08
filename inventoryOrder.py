# Inventory Ordering System
# This will receive user input through textboxes and write to a text file

import tkinter as tk
from settingsMenu import default_settings
from tkinter import ttk
from inventory_master import InventoryItem as inv

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

        #Label Declarations
        self.orderLabel = tk.Label(self, text="Create New Order")
        self.nameLabel = tk.Label(self, text = "Enter Item name")
        self.itemQty = tk.Label(self, text="Insert Item Quantity")

        #User Entry Declarations
        self.nameEntry = ttk.Entry(self, textvariable = self.nameStr)
        self.qtyEntry = ttk.Entry(self, textvariable = self.qtyStr)

    #Function to submit currently held variables into txt file
    def submit():
        name = self.nameStr.get()
        qty=self.qtyStr.get()
        
        #Write input to file
        #with open("OrderList.txt", "a") as f:
        #    f.write(item)
        #with open("OrderList.txt", "a") as f:
        #    f.write(qty)
        #with open("OrderList.txt", "a") as f:
        #    f.write(name)

        inv.add_stock(name, qty)

        print("The item is : " + name)
        print("The Quantity is : " + qty)
        
        
        nameStr.set("")
        qtyStr.set("")


    #open and read the file after the appending:
    with open("orderList.txt") as f:
    print(f.read())

    #Variable calls
    orderLabel.pack()

    nameLabel.pack()
    nameEntry.pack()

    itemQty.pack()
    qtyEntry.pack()

    #Submit button
    sub_btn=tk.Button(root,text = 'Submit', command = submit)
    sub_btn.pack()

    ## Run Program
    root.mainloop()