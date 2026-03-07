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




## open window
root.mainloop()