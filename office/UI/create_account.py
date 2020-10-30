import tkinter as tk


def create_account(msg):
    print(msg)


def set_frame(root):
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

    create_btn = tk.Button(create_frame, text='Create account', command=lambda: create_account(account_no.get()))
    create_btn.config(bg='green')
    create_btn.grid(row=4, column=1, sticky='w', pady=5)
