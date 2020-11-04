import tkinter as tk
from tkinter import messagebox


def withdraw_money(account_no, amount, user):
    if account_no == '' or amount == '':
        messagebox.showwarning(message='Please complete the form', title='Incomplete form')
    else:
        status = user.withdraw_money(account_no, amount)

        if status == 5:
            messagebox.showwarning(message='Account does not exists', title='Missing account')
        elif status == 3:
            messagebox.showerror(message='An error has occurred in the database', title='Database error')
        elif status == 1:
            messagebox.showinfo(message='Successful transaction', title='Ok')


def set_frame(root, user):
    consignment_frame = tk.Frame(root)
    consignment_frame.config(borderwidth=5, highlightbackground='black', highlightthickness=1)
    consignment_frame.grid(row=1, column=1, sticky='n', padx=2, pady=2)

    # Frame title
    tk.Label(consignment_frame, text='Withdraw money').grid(row=0, column=0, sticky='w', padx=5, pady=5)

    # Withdraw account form
    tk.Label(consignment_frame, text='Account number').grid(row=1, column=0, sticky='w', padx=5, pady=5)
    account_no = tk.Entry(consignment_frame)
    account_no.grid(row=1, column=1)

    tk.Label(consignment_frame, text='Amount to withdraw').grid(row=2, column=0, sticky='w', padx=5, pady=5)
    amount = tk.Entry(consignment_frame)
    amount.grid(row=2, column=1)

    withdraw_btn = tk.Button(consignment_frame, text='Withdraw money',
                             command=lambda: withdraw_money(account_no.get(), amount.get(), user))
    withdraw_btn.config(bg='#115e76')
    withdraw_btn.grid(row=4, column=1, sticky='w', pady=5)
