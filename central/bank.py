import Pyro4
from central import db_manager as db
from central import caesar_cypher
from central.account import Account


# This class models the bank data
@Pyro4.expose
class Bank:

    def __init__(self, accounts, offices):
        self.accounts = accounts
        self.offices = offices

    @staticmethod
    def search_user(username, password, shift):
        username = caesar_cypher.process_text(username, shift, 'DECRYPT')
        password = caesar_cypher.process_text(password, shift, 'DECRYPT')

        print(username, ':', username)
        print(password, ':', password)

        user = db.search_user(username, password)
        print(user)

        if len(user) > 0:
            for i in range(0, len(user)):
                user[i] = caesar_cypher.process_text(user[i], shift, 'ENCRYPT')

        print(user)
        return user

    # create_account returns:
    # 5 -> If the account is already exists
    # 3 -> If a database error has occurred
    # 1 -> If the account creation is done
    def create_account(self, account, owner, mount, shift):
        # TODO: validate the user permissions (initialize the employees)
        account = caesar_cypher.process_text(account, shift, 'DECRYPT')
        if account in self.accounts:
            return 5
        else:
            owner = caesar_cypher.process_text(owner, shift, 'DECRYPT')
            mount = caesar_cypher.process_text(mount, shift, 'DECRYPT')
            created_at = db.create_account(account, mount, owner)

            if created_at != '':
                self.accounts[account] = Account(account, mount, owner, '', created_at)
                return 1
            else:
                return 3

    # delete_account returns:
    # 5 -> If the account is not found
    # 3 -> If a database error has occurred
    # 1 -> If the account is deleted
    def delete_account(self, account, shift):
        account = caesar_cypher.process_text(account, shift, 'DECRYPT')
        if account in self.accounts:
            if db.delete_account(account):
                self.accounts.pop(account)
                return 1
            else:
                return 3
        else:
            return 5

    def update_account(self, account, new_owner, shift):
        pass

    def add_money(self, account, amount, shift):
        pass

    def withdraw_money(self, account, shift):
        pass

    def get_money(self, account, shift):
        pass

    # get_account returns:
    # '5' -> If the account_no is not found
    # account_info -> If the account exists
    def get_account(self, account_no, shift):
        account_no = caesar_cypher.process_text(account_no, shift, 'DECRYPT')
        if account_no in self.accounts:
            # Encrypt the dictionary values
            account_info = self.accounts[account_no].get_info()
            for property in account_info:
                account_info[property] = caesar_cypher.process_text(account_info[property], shift, 'ENCRYPT')

            return account_info
        else:
            return '5'

    def __process_text(self, msg, shift):
        pass


# In the main method the Remote Object is registered with the "central_bank" name
def main():
    daemon = Pyro4.Daemon()

    uri = daemon.register(Bank(db.get_accounts(), db.get_offices()))
    name_server = Pyro4.locateNS()
    name_server.register('central_bank', uri)

    daemon.requestLoop()


if __name__ == '__main__':
    main()
