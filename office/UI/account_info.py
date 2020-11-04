import tkinter as tk
from tkinter import messagebox


def show_account(account_no, account_info, user):
    info = user.get_account(account_no)

    if info != '5':
        info_txt = 'ACCOUNT INFO:\n\n'

        # TODO: maybe I need change the way it is encrypted the account info
        for data in info:
            info_txt += f'{data} : {info[data]}\n'

        account_info.delete(1.0, tk.END)
        account_info.insert(tk.INSERT, info_txt)
    else:
        messagebox.showwarning(message='Account does not exists', title='Not found')


def set_frame(root, user):
    search_frame = tk.Frame(root)
    search_frame.config(borderwidth=5, highlightbackground='black', highlightthickness=1)
    search_frame.grid(row=0, column=3, sticky='n', padx=2, pady=2, rowspan=4)

    # Frame title
    tk.Label(search_frame, text='Search account').grid(row=0, column=0, sticky='w', padx=5, pady=5)

    # Show account form
    tk.Label(search_frame, text='Account number').grid(row=1, column=0, sticky='w', padx=5, pady=5)
    account_no = tk.Entry(search_frame)
    account_no.grid(row=1, column=1)

    info = tk.Text(search_frame, width=35, height=20)
    info.grid(row=5, column=0, sticky='w', pady=5, columnspan=2)

    show_btn = tk.Button(search_frame, text='Search account',
                         command=lambda: show_account(account_no.get(), info, user))
    show_btn.config(bg='#115e76')
    show_btn.grid(row=4, column=1, sticky='w', pady=5)
