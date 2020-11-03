class Account:

    def __init__(self, account_no, amount, owner, password, created_at):
        self.account_no = account_no
        self.amount = amount
        self.owner = owner
        self.password = password
        self.created_at = created_at

    def get_account_no(self):
        return self.account_no

    def get_amount(self):
        return self.amount

    def set_amount(self, mount):
        self.amount = mount

    def get_owner(self):
        return self.owner

    def set_owner(self, new_owner):
        self.owner = new_owner

    def get_password(self):
        return self.password

    def get_created_at(self):
        return self.created_at

    def get_info(self):
        return {
            'account_no': self.account_no,
            'amount': self.amount,
            'owner': self.owner,
            'created_at': self.created_at
        }