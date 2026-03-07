import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title('Tkinter Window - Center')
root.geometry("500x500")


orderLabel = tk.Label(root, text="Create New Order")

name_entry = ttk.Entry(root)

orderLabel.pack()
name_entry.pack()
## open window
root.mainloop()