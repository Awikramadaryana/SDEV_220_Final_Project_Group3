# Inventory Ordering System
# This will receive user input through textboxes and write to a text file

import tkinter as tk
from settingsMenu import default_settings
from tkinter import ttk
from inventory_master import InventoryItem as inv
from inventory_master import default_inventory

class addMenu(tk.Tk):
    def __init__(self, screenName = None, baseName = None, className = "Tk", useTk = True, sync = False, use = None):
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.title("Inventory Menu")
        self.geometry("500x500")
        self.stock_items = []
        self.configure(bg=default_settings.background)

        #declare string variables to store item details
        self.nameStr = tk.StringVar(self)
        self.maxStr = tk.StringVar(self)
        self.currentStr = tk.StringVar(self)
        self.minStr = tk.StringVar(self)


        #Label Declarations
        self.orderLabel = tk.Label(self, text="Add New Item")
        self.nameLabel = tk.Label(self, text = "Enter Item name")
        self.itemMax = tk.Label(self, text="Insert Maximum Stock Count")
        self.itemCurrent = tk.Label(self, text = "Insert Current Stock Count")
        self.itemMinimum = tk.Label(self, text = "Insert Minimum Stock Count")


        #User Entry Declarations
        self.nameEntry = ttk.Entry(self, textvariable = self.nameStr)
        self.maxEntry = ttk.Entry(self, textvariable = self.maxStr)
        self.currentEntry = ttk.Entry(self, textvariable= self.currentStr)
        self.minEntry = ttk.Entry(self, textvariable= self.minStr)

        #UI elements
        self.orderLabel.pack()

        self.nameLabel.pack()
        self.nameEntry.pack()

        self.itemMax.pack()
        self.maxEntry.pack()

        self.itemCurrent.pack()
        self.currentEntry.pack()

        self.itemMinimum.pack()
        self.minEntry.pack()

        #Submit button
        sub_btn=tk.Button(self,text = 'Submit', command = self.submit)
        sub_btn.pack()
        

    #Function to submit currently held variables into dictionary
    def submit(self):
        name = self.nameStr.get()
        maximum = self.maxStr.get()
        current = self.currentStr.get()
        minimum = self.minStr.get()

        print("The item is : " + name)
        print("The max quantity is : " + maximum)
        print("The current quantity is : " + current)
        print("The min quantity is : " + minimum)

        #Set stored string variables back to empty strings
        self.nameStr.set("")
        self.maxStr.set("")
        self.currentStr.set("")
        self.minStr.set("")