import tkinter as tk
from office.UI import create_account
from office.UI import delete_account
from office.UI import update_account
from office.UI import consing_money
from office.UI import withdraw_money
from office.UI import account_info

root = tk.Tk()

# Settings
root.title('Bank: ')
root.config(borderwidth=5)
root.resizable(0, 0)

create_account.set_frame(root)
delete_account.set_frame(root)
update_account.set_frame(root)
consing_money.set_frame(root)
withdraw_money.set_frame(root)
account_info.set_frame(root)

root.mainloop()
