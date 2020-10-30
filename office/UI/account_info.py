import tkinter as tk


def create_account(msg):
    print(msg)


def set_frame(root):
    search_frame = tk.Frame(root)
    search_frame.config(borderwidth=5, highlightbackground='black', highlightthickness=1)
    search_frame.grid(row=0, column=3, sticky='n', padx=2, pady=2, rowspan=4)

    # Frame title
    tk.Label(search_frame, text='Search account').grid(row=0, column=0, sticky='w', padx=5, pady=5)

    # Create account form
    tk.Label(search_frame, text='Account number').grid(row=1, column=0, sticky='w', padx=5, pady=5)
    account_no = tk.Entry(search_frame)
    account_no.grid(row=1, column=1)

    create_btn = tk.Button(search_frame, text='Search account', command=lambda: create_account(account_no.get()))
    create_btn.config(bg='#115e76')
    create_btn.grid(row=4, column=1, sticky='w', pady=5)

    account_info = tk.Text(search_frame, width=35, height=20)
    account_info.grid(row=5, column=0, sticky='w', pady=5, columnspan=2)
