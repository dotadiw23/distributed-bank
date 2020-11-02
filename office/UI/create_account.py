import tkinter as tk
from tkinter import messagebox
from office import caesar_cypher
from random import randint


def create_account(account_no, account_owner, starting_amount, central_bank):
    if account_no == '' or account_owner == '' or starting_amount == '':
        messagebox.showwarning(message='Please complete the form', title='Incomplete form')
    else:
        # Encrypt the request data
        shift = randint(1, 65)
        account_no = caesar_cypher.process_text(account_no, shift, 'ENCRYPT')
        account_owner = caesar_cypher.process_text(account_owner, shift, 'ENCRYPT')
        starting_amount = caesar_cypher.process_text(starting_amount, shift, 'ENCRYPT')

        status = central_bank.create_account(account_no, account_owner, starting_amount, shift)

        if status == 5:
            messagebox.showwarning(message='Account already exists', title='Creation error')
        elif status == 3:
            messagebox.showerror(message='An error has occurred in the database', title='Database error')
        elif status == 1:
            messagebox.showinfo(message='Account created successfully', title='Ok')


def set_frame(root, central_bank):
    create_frame = tk.Frame(root)
    create_frame.config(borderwidth=5, highlightbackground='black', highlightthickness=1)
    create_frame.grid(row=0, column=0, sticky='n', padx=2, pady=2)

    # Frame title
    tk.Label(create_frame, text='Create account').grid(row=0, column=0, sticky='w', padx=5, pady=5)

    # Create account form
    tk.Label(create_frame, text='Account number').grid(row=1, column=0, sticky='w', padx=5, pady=5)
    account_no = tk.Entry(create_frame)
    account_no.grid(row=1, column=1)

    tk.Label(create_frame, text='Account owner').grid(row=2, column=0, sticky='w', padx=5, pady=5)
    account_owner = tk.Entry(create_frame)
    account_owner.grid(row=2, column=1)

    tk.Label(create_frame, text='Starting amount').grid(row=3, column=0, sticky='w', padx=5, pady=5)
    starting_amount = tk.Entry(create_frame)
    starting_amount.grid(row=3, column=1)

    create_btn = tk.Button(create_frame, text='Create account', command=lambda: create_account(account_no.get(), account_owner.get(), starting_amount.get(), central_bank))
    create_btn.config(bg='green')
    create_btn.grid(row=4, column=1, sticky='w', pady=5)
