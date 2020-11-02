import tkinter as tk
from office.UI import start_app


root = tk.Tk()

# Settings
root.title('Bank: ')
root.config(borderwidth=5)
root.resizable(0, 0)

start_app.set_frame(root)

root.mainloop()
