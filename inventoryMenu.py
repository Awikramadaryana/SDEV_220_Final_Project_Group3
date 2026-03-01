"""
File Name: inventoryMenu.py
Author: Team 3
Date last updated: 2/23/2026
Purpose: Provide Inventory interaction menu
"""

import tkinter as tk
from cafeInventory import cafe_inventory

class inventoryMenu(tk.Tk):
    def __init__(self, screenName = None, baseName = None, className = "Tk", useTk = True, sync = False, use = None):
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.title("Inventory Menu")
        self.geometry("500x500")

        # prepping options for the drop down menu
        stockItems = [cafe_inventory[1]["name"], cafe_inventory[2]["name"], cafe_inventory[3]["name"], cafe_inventory[4]["name"],
                      cafe_inventory[5]["name"], cafe_inventory[6]["name"], cafe_inventory[7]["name"], cafe_inventory[8]["name"],
                      cafe_inventory[9]["name"]]
        selectedOption = tk.StringVar(self)
        selectedOption.set(stockItems[0])
        selectedData = tk.IntVar(self)

        def updateMenu():
            print("Hello world")

        # Actual Menu
        tk.Label(self, text="Welcome to Inventory Management").pack()
        tk.Label(self, text="Pick an Inventory Item").pack()
        tk.OptionMenu(self, selectedOption, *stockItems).pack()
        tk.Button(self, text="Show Data for Item").pack()
        # lbl = tk.Label(self, text=)
        