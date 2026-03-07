import tkinter as tk

class SettingsMenu(tk.Toplevel):

    def __init__(self, master=None):
        super().__init__(master)

        self.title("Settings")
        self.geometry("400x300")

        self.darkMode = tk.BooleanVar()
        self.autoSave = tk.BooleanVar()
        self.defaultStock = tk.IntVar(value=10)

        tk.Label(self, text="Application Settings").pack()

        tk.Checkbutton(self, text="Enable Dark Mode", variable=self.darkMode).pack()
        tk.Checkbutton(self, text="Enable Auto Save", variable=self.autoSave).pack()

        tk.Label(self, text="Default Restock Amount").pack()
        tk.Entry(self, textvariable=self.defaultStock).pack()

        tk.Button(self, text="Save Settings", command=self.save_settings).pack()

    def save_settings(self):
        print("Dark Mode:", self.darkMode.get())
        print("Auto Save:", self.autoSave.get())
        print("Default Restock:", self.defaultStock.get())


if __name__ == "__main__":
    root = tk.Tk()
    SettingsMenu(root)
    root.mainloop()