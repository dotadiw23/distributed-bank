import tkinter as tk
from tkinter import messagebox


def update_account(account_no, new_owner, user):
    if account_no == '' or new_owner == '':
        messagebox.showwarning(message='Please complete the form', title='Incomplete form')
    else:

        status = user.update_account(account_no, new_owner)

        if status == 5:
            messagebox.showwarning(message='Account is not found', title='Missing account')
        elif status == 3:
            messagebox.showerror(message='An error has occurred in the database', title='Database error')
        elif status == 1:
            messagebox.showinfo(message='Account updated successfully', title='Update')


def set_frame(root, user):
    update_frame = tk.Frame(root)
    update_frame.config(borderwidth=5, highlightbackground='black', highlightthickness=1)
    update_frame.grid(row=1, column=0, sticky='n', padx=2, pady=2)

    # Frame title
    tk.Label(update_frame, text='Update account').grid(row=0, column=0, sticky='w', padx=5, pady=5)

    # Update account form
    tk.Label(update_frame, text='Account number').grid(row=1, column=0, sticky='w', padx=5, pady=5)
    account_no = tk.Entry(update_frame)
    account_no.grid(row=1, column=1)

    tk.Label(update_frame, text='New owner').grid(row=2, column=0, sticky='w', padx=5, pady=5)
    new_owner = tk.Entry(update_frame)
    new_owner.grid(row=2, column=1)

    update_btn = tk.Button(update_frame, text='Update account',
                           command=lambda: update_account(account_no.get(), new_owner.get(), user))
    update_btn.config(bg='#115e76')
    update_btn.grid(row=4, column=1, sticky='w', pady=5)
