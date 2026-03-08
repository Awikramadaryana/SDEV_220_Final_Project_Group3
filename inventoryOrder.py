# Inventory Ordering System
# This will receive user input through textboxes and write to a text file

import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title('Tkinter Window - Center')
root.geometry("500x500")

#Label Declarations
orderLabel = tk.Label(root, text="Create New Order")
itemCode = tk.Label(root, text="Insert Item Code")
itemQty = tk.Label(root, text="Insert Item Quantity")

#User Entry Declarations
codeEntry = ttk.Entry(root)
qtyEntry = ttk.Entry(root)

#Variable calls
orderLabel.pack()

itemCode.pack()
codeEntry.pack()

itemQty.pack()
qtyEntry.pack()

def fetch(entry, label):
    label['text'] = entry.get()

def submit():

    item=itemCode.get()
    qty=itemQty.get()
    
    #Write input to file
    with open("OrderList.txt", "a") as f:
        f.write(item)
    with open("OrderList.txt", "a") as f:
        f.write(qty)

    print("The item is : " + item)
    print("The Quantity is : " + qty)
    
    itemCode.set("")
    itemQty.set("")


#open and read the file after the appending:
with open("orderList.txt") as f:
  print(f.read())

#Submit button
sub_btn=tk.Button(root,text = 'Submit', command = submit)
sub_btn.pack()

## Run Program
root.mainloop()