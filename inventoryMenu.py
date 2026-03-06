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
        """
        self.stockItems = [cafe_inventory[1]["name"], cafe_inventory[2]["name"], cafe_inventory[3]["name"], cafe_inventory[4]["name"],
                      cafe_inventory[5]["name"], cafe_inventory[6]["name"], cafe_inventory[7]["name"], cafe_inventory[8]["name"],
                      cafe_inventory[9]["name"]]
        """
        self.selectedOption = tk.StringVar(self)
        self.selectedOption.set(self.stock_items[i])
        self.selectedData = tk.IntVar(self)
        self.selectedIndex = 0

        # Actual Menu
        tk.Label(self, text="Welcome to Inventory Management").pack()
        tk.Label(self, text="Pick an Inventory Item").pack()
        tk.OptionMenu(self, self.selectedOption, *self.stock_items, command= self.updateMenu()).pack()
        self.output_label = tk.Label(self, text="Item Pending")
        self.output_label.pack()
        #tk.Button(self, text="Show Data for Item").pack()
        # lbl = tk.Label(self, text=)

    def create_widgets(self):
        paddings = {'padx': 5, 'pady': 5}


    def updateMenu(self):
        print("Hello world")
        selectedItem = self.selectedOption.get()
        print(selectedItem)
        self.output_label = (f'You selected: {self.selectedOption.get()}')
        """match selectedOption:
                case "coffee_beans":
                    selectedIndex == 1
                case "tea_bags":
                    selectedIndex == 2
                case "milk":
                    selectedIndex == 3
                case "sugar":
                    selectedIndex == 4
                case "croissant":
                    selectedIndex == 5
                case "muffin_box":
                    selectedIndex == 6
                case "sandwich":
                    selectedIndex == 7
                case "paper_cups":
                    selectedIndex == 8
                case "napkins":
                    selectedIndex == 9
            print(selectedIndex)
            """
        