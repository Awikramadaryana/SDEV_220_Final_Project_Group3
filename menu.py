"""
Project Name: Group2Project.py
Author: Brenden Melody, Darcy Ralstin, Cailli Church
Date last updated: 5/10/2025
Description: Program is designed to play a version of Pong that allows players
            to choose their names and colors. This module operates the main menu to actually start the game
"""


import tkinter as tk
import inventoryMenu
from inventory_master import CafeInventory, InventoryItem, inventory

"""
This module actually initializes the main menu with the 3 main buttons to start the game
change the name of the players, and to close the game.
"""

def main():
    mainMenu = tk.Tk()
    mainMenu.title("Pong")
    mainMenu.geometry("500x500")
    mainMenu['background'] = "white"

    # creating welcome label and buttons
    welcomeMessage = tk.Label(mainMenu, text="Welcome to Coffee Shop!")
    orderButton = tk.Button(mainMenu, text="Order")
    inventoryButton = tk.Button(mainMenu, text="Inventory", command=lambda: inventoryMenu.inventoryMenu())
    settingsButton = tk.Button(mainMenu, text ="Settings")
    exitButton = tk.Button(mainMenu, text="Exit", command=mainMenu.quit)

    
    welcomeMessage.pack()
    orderButton.pack()
    inventoryButton.pack()
    settingsButton.pack()
    exitButton.pack()
    mainMenu.mainloop()
    

if __name__ == '__main__':
    inventory.add_item("Coffee Beans", 50, 25, 10)
    inventory.add_item("Milk", 20, 15, 5)
    inventory.add_item("Sugar", 30, 20, 8)
    inventory.display_inventory()
    #current_inventory = CafeInventory()
    #current_inventory.add_item("Coffee Beans", 50, 10)
    #current_inventory.add_item("Milk", 20, 5)
    #current_inventory.add_item("Sugar", 30, 8)
    main()