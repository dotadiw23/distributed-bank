import tkinter as tk
from tkinter import messagebox
from random import randint

from office import caesar_cypher


def create_account(account_no, account_info, central_bank):
    print(account_no)
    shift = randint(0, 67)
    account_no = caesar_cypher.process_text(account_no, shift, 'ENCRYPT')
    info = central_bank.get_account(account_no, shift)

    info_txt = 'ACCOUNT INFO:\n\n'
    if info != '5':
        # TODO: maybe I need change the way it is encrypted the account info
        for property in info:
            info[property] = caesar_cypher.process_text(info[property], shift, 'DECRYPT')
            info_txt += f'{property} : {info[property]}\n'

        account_info.delete(1.0, tk.END)
        account_info.insert(tk.INSERT, info_txt)
    else:
        messagebox.showwarning(message='Account does not exists', title='Not found')


def set_frame(root, central_bank):
    search_frame = tk.Frame(root)
    search_frame.config(borderwidth=5, highlightbackground='black', highlightthickness=1)
    search_frame.grid(row=0, column=3, sticky='n', padx=2, pady=2, rowspan=4)

    # Frame title
    tk.Label(search_frame, text='Search account').grid(row=0, column=0, sticky='w', padx=5, pady=5)

    # Create account form
    tk.Label(search_frame, text='Account number').grid(row=1, column=0, sticky='w', padx=5, pady=5)
    account_no = tk.Entry(search_frame)
    account_no.grid(row=1, column=1)

    account_info = tk.StringVar(search_frame)

    info = tk.Text(search_frame, width=35, height=20)
    info.grid(row=5, column=0, sticky='w', pady=5, columnspan=2)

    create_btn = tk.Button(search_frame, text='Search account',
                           command=lambda: create_account(account_no.get(), info, central_bank))
    create_btn.config(bg='#115e76')
    create_btn.grid(row=4, column=1, sticky='w', pady=5)
