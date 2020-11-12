import tkinter as tk
from tkinter import messagebox


def delete_account(account_no, user):
    if account_no != '':
        if messagebox.askyesno(message=f'Are you sure to delete account: {account_no}', title='Continue?'):
            status = user.delete_account(account_no)

            if status == 5:
                messagebox.showwarning(message='Account is not found', title='Not found')
            elif status == 3:
                messagebox.showerror(message='An error has occurred in the database', title='Database error')
            elif status == 1:
                messagebox.showinfo(message='Account deleted successfully', title='Ok')

    else:
        messagebox.showwarning(message='Please complete the form', title='Incomplete form')


def set_frame(root, user):
    delete_frame = tk.Frame(root)
    delete_frame.config(borderwidth=5, highlightbackground='black', highlightthickness=1)
    delete_frame.grid(row=3, column=0, sticky='n', padx=2, pady=2)

    # Frame title
    tk.Label(delete_frame, text='Delete account').grid(row=0, column=0, sticky='w', padx=5, pady=5)

    # Delete account form
    tk.Label(delete_frame, text='Account number').grid(row=1, column=0, sticky='w', padx=5, pady=5)
    account_no = tk.Entry(delete_frame)
    account_no.grid(row=1, column=1)

    delete_btn = tk.Button(delete_frame, text='Delete account', command=lambda: delete_account(account_no.get(), user))
    delete_btn.config(bg='red')
    delete_btn.grid(row=4, column=1, sticky='w', pady=5)
    delete_btn.bind()
