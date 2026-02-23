"""
File Name: inventoryMenu.py
Author: Team 3
Date last updated: 2/23/2026
Purpose: Provide Inventory interaction menu
"""

import tkinter as tk

class inventoryMenu(tk.Tk):
    def __init__(self, screenName = None, baseName = None, className = "Tk", useTk = True, sync = False, use = None):
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.title("Inventory Menu")

        # Actual Menu
        tk.Label(self, text="Welcome to Inventory Management").pack(pady=10)
        