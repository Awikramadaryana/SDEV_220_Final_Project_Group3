import tkinter as tk

class SettingsMenu(tk.Toplevel):

    def __init__(self, master=None):
        #initializing window
        super().__init__(master)
        self.title("Settings")
        self.geometry("400x300")
        self.configure(bg=default_settings.background)

        # initializing variables
        self.darkMode = tk.BooleanVar()
        self.autoSave = tk.BooleanVar()
        self.defaultStock = tk.IntVar(value=10)

        #initializing gui interface
        tk.Label(self, text="Application Settings").pack()

        # creating check button for the dark mode version of the code
        tk.Checkbutton(self, text="Enable Dark Mode", variable=self.darkMode).pack()
        tk.Checkbutton(self, text="Enable Auto Save", variable=self.autoSave).pack()

        tk.Label(self, text="Default Restock Amount").pack()
        tk.Entry(self, textvariable=self.defaultStock).pack()

        tk.Button(self, text="Save Settings", command=self.save_settings).pack()

    # function allows selected settings to be saved to the default_settings configuration class instantiated previously
    def save_settings(self):
        print("Dark Mode:", self.darkMode.get())
        print("Auto Save:", self.autoSave.get())
        print("Default Restock:", self.defaultStock.get())
        self.destroy()


# settings_config class creates class object that will allow settings to transfer between windows.
class settings_config:
    def __init__(self):
        self.background = 'white'
        self.default_stock = 0
        self.auto_save = False
        
    def dark_mode (self, enable):
        if enable == True:
            self.background = 'black'
        else:
            self.background = 'white'


if __name__ == "__main__":
    root = tk.Tk()
    SettingsMenu(root)
    root.mainloop()
    
# instantiating settings_config object as defaults
default_settings = settings_config()