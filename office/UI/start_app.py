import tkinter as tk
from tkinter import messagebox
from office.UI import create_account, delete_account, update_account, consing_money, withdraw_money, account_info
import Pyro4
from office.model import employees
from office import caesar_cypher
from random import randint

# Pyro setup
ns = Pyro4.locateNS()
uri = ns.lookup('central_bank')
central_bank = Pyro4.Proxy(uri)

user = object


# Search in the central database the access credentials
def authenticate_user(username, password):
    shift = randint(0, 65)

    # Encrypt the request args
    encrypted_username = caesar_cypher.process_text(username, shift, 'ENCRYPT')
    encrypted_password = caesar_cypher.process_text(password, shift, 'ENCRYPT')

    credentials = central_bank.search_user(encrypted_username, encrypted_password, shift)

    print(credentials)
    # Decrypt the response
    if len(credentials) > 0:
        for i in range(0, len(credentials)):
            credentials[i] = caesar_cypher.process_text(credentials[i], shift, 'DECRYPT')

    print(credentials)
    return credentials


# ----------------------- UI -----------------------
def login(username, password, root):
    credentials = authenticate_user(username, password)
    if len(credentials) > 0:

        global user

        if credentials[3] == '2':
            user = employees.Manager(credentials[0], credentials[1], credentials[2], credentials[3])
        elif credentials[3] == '1':
            user = employees.Cashier(credentials[0], credentials[1], credentials[2], credentials[3])

        root.destroy()

        # ------------------- Application Frame -------------------
        root = tk.Tk()

        # Settings
        root.title('Bank: ')
        root.config(borderwidth=5)
        root.resizable(0, 0)

        global central_bank

        if user.get_permissions() == '2':
            create_account.set_frame(root, central_bank)
            delete_account.set_frame(root, central_bank)
            update_account.set_frame(root)

        consing_money.set_frame(root)
        withdraw_money.set_frame(root)
        account_info.set_frame(root)

        root.mainloop()
    else:
        messagebox.showerror(message='Invalid login credentials', title='Login error')


def set_frame(root):
    # ------------------- Login Frame -------------------
    login_frame = tk.Frame(root)
    login_frame.pack()
    login_frame.config(width=480, height=320, borderwidth=5, highlightbackground='black', highlightthickness=1)

    # Frame title
    tk.Label(login_frame, text="Welcome").grid(row=0, column=1, padx=15, pady=15)

    # Create account form
    tk.Label(login_frame, text='Username').grid(row=1, column=0, sticky='w', padx=5, pady=5)
    username = tk.Entry(login_frame)
    username.grid(row=1, column=1)

    tk.Label(login_frame, text='Password').grid(row=2, column=0, sticky='w', padx=5, pady=5)
    password = tk.Entry(login_frame)
    password.config(show='*')
    password.grid(row=2, column=1)

    login_btn = tk.Button(login_frame, text='Login', command=lambda: login(username.get(), password.get(), root))
    login_btn.grid(row=2, column=3, padx=5, pady=5)
