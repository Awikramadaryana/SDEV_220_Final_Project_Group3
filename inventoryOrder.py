# Inventory Ordering System
# This will receive user input through textboxes and write to a text file

import tkinter as tk
from tkinter import ttk
from inventory_master import CafeInventory


root = tk.Tk()
root.title('Tkinter Window - Center')
root.geometry("500x500")

#declare string variables to store item details
nameStr = tk.StringVar()
codeStr = tk.StringVar()
qtyStr = tk.StringVar()

#Label Declarations
orderLabel = tk.Label(root, text="Create New Order")
nameLabel = tk.Label(root, text = "Enter Item name")
itemCode = tk.Label(root, text="Insert Item Code")
itemQty = tk.Label(root, text="Insert Item Quantity")

#User Entry Declarations
nameEntry = ttk.Entry(root, textvariable = nameStr)
codeEntry = ttk.Entry(root, textvariable = codeStr)
qtyEntry = ttk.Entry(root, textvariable = qtyStr)

#Function to submit currently held variables into txt file
def submit():
    name = nameStr.get()
    item=codeStr.get()
    qty=qtyStr.get()
    
    #Write input to file
    with open("OrderList.txt", "a") as f:
        f.write(item)
    with open("OrderList.txt", "a") as f:
        f.write(qty)
    with open("OrderList.txt", "a") as f:
        f.write(name)

    print("The item is : " + name)
    print("The item code : " + item)
    print("The Quantity is : " + qty)
    
    
    nameStr.set("")
    codeStr.set("")
    qtyStr.set("")


#open and read the file after the appending:
with open("orderList.txt") as f:
  print(f.read())

#Variable calls
orderLabel.pack()

nameLabel.pack()
nameEntry.pack()

itemCode.pack()
codeEntry.pack()

itemQty.pack()
qtyEntry.pack()

#Submit button
sub_btn=tk.Button(root,text = 'Submit', command = submit)
sub_btn.pack()

## Run Program
root.mainloop()