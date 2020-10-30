import tkinter as tk


def delete_account(msg):
    print(msg)


def set_frame(root):
    update_frame = tk.Frame(root)
    update_frame.config(borderwidth=5, highlightbackground='black', highlightthickness=1)
    update_frame.grid(row=1, column=0, sticky='n', padx=2, pady=2)

    # Frame title
    tk.Label(update_frame, text='Update account').grid(row=0, column=0, sticky='w', padx=5, pady=5)

    # Create account form
    tk.Label(update_frame, text='Account number').grid(row=1, column=0, sticky='w', padx=5, pady=5)
    account_no = tk.Entry(update_frame)
    account_no.grid(row=1, column=1)

    tk.Label(update_frame, text='New owner').grid(row=2, column=0, sticky='w', padx=5, pady=5)
    new_owner = tk.Entry(update_frame)
    new_owner.grid(row=2, column=1)

    update_btn = tk.Button(update_frame, text='Update account', command=lambda: delete_account(account_no.get()))
    update_btn.config(bg='#115e76')
    update_btn.grid(row=4, column=1, sticky='w', pady=5)
