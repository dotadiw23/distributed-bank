class Account:

    def __init__(self, account_no, mount, owner):
        self.account_no = account_no
        self.mount = mount
        self.owner = owner

    def get_account_no(self):
        return self.account_no

    def get_mount(self):
        return self.account_no

    def set_mount(self, mount):
        self.mount = mount

    def get_owner(self):
        return self.owner

    def set_owner(self, new_owner):
        self.owner = new_owner