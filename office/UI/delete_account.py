import tkinter as tk


def delete_account(msg):
    print(msg)


def set_frame(root):
    delete_frame = tk.Frame(root)
    delete_frame.config(borderwidth=5, highlightbackground='black', highlightthickness=1)
    delete_frame.grid(row=3, column=0, sticky='n', padx=2, pady=2)

    # Frame title
    tk.Label(delete_frame, text='Delete account').grid(row=0, column=0, sticky='w', padx=5, pady=5)

    # Create account form
    tk.Label(delete_frame, text='Account number').grid(row=1, column=0, sticky='w', padx=5, pady=5)
    account_no = tk.Entry(delete_frame)
    account_no.grid(row=1, column=1)

    delete_btn = tk.Button(delete_frame, text='Delete account', command=lambda: delete_account(account_no.get()))
    delete_btn.config(bg='red')
    delete_btn.grid(row=4, column=1, sticky='w', pady=5)
    delete_btn.bind()
