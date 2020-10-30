import tkinter as tk


def consign_money(msg):
    print(msg)


def set_frame(root):
    consignment_frame = tk.Frame(root)
    consignment_frame.config(borderwidth=5, highlightbackground='black', highlightthickness=1)
    consignment_frame.grid(row=0, column=1, sticky='n', padx=2, pady=2)

    # Frame title
    tk.Label(consignment_frame, text='Consign money').grid(row=0, column=0, sticky='w', padx=5, pady=5)

    # Create account form
    tk.Label(consignment_frame, text='Account number').grid(row=1, column=0, sticky='w', padx=5, pady=5)
    account_no = tk.Entry(consignment_frame)
    account_no.grid(row=1, column=1)

    tk.Label(consignment_frame, text='Amount to consign').grid(row=2, column=0, sticky='w', padx=5, pady=5)
    amount = tk.Entry(consignment_frame)
    amount.grid(row=2, column=1)

    consign_btn = tk.Button(consignment_frame, text='Consign money', command=lambda: consign_money(account_no.get()))
    consign_btn.config(bg='#115e76')
    consign_btn.grid(row=4, column=1, sticky='w', pady=5)
