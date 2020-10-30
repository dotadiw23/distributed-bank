import Pyro4
from central import db_manager as db


# This class models the bank data
class Bank:

    def __init__(self, accounts, offices):
        self.accounts = accounts
        self.offices = offices

    def create_account(self, account, amount, date, shift):
        pass

    def delete_account(self, account, shift):
        pass

    def update_account(self, account, new_owner, shift):
        pass

    def add_money(self, account, amount, shift):
        pass

    def withdraw_money(self, account, shift):
        pass

    def get_money(self, account, shift):
        pass

    def __process_text(self, msg, shift):
        pass


# In the main method the Remote Object is registered with the "central_bank" name
def main():
    daemon = Pyro4.Daemon()

    uri = daemon.register(Bank(db.get_accounts(), db.get_offices()))
    name_server = Pyro4.locateNS()
    name_server.register('central_bank', uri)


if __name__ == '__main__':
    main()
