from office import caesar_cypher
from random import randint


class Employee:

    def __init__(self, username, password, permissions, central_bank):
        self._username = username
        self._password = password
        self._permissions = permissions
        self._central_bank = central_bank

    def get_username(self):
        return self._username

    def get_password(self):
        return self._password

    def get_permissions(self):
        return self._permissions

    def get_account(self, account_no):
        # Encrypt the request data
        shift = randint(1, 67)
        account_no = caesar_cypher.process_text(account_no, shift, 'ENCRYPT')

        info = self._central_bank.get_account(account_no, shift)

        if info != '5':
            # Decrypt the server response
            for data in info:
                info[data] = caesar_cypher.process_text(info[data], shift, 'DECRYPT')

        return info

    def consign_money(self, account_no, amount):
        shift = randint(0, 67)
        account_no = caesar_cypher.process_text(account_no, shift, 'ENCRYPT')
        amount = caesar_cypher.process_text(amount, shift, 'ENCRYPT')

        return self._central_bank.add_money(account_no, amount, shift)

    def withdraw_money(self, account_no, amount):
        shift = randint(1, 67)
        account_no = caesar_cypher.process_text(account_no, shift, 'ENCRYPT')
        amount = caesar_cypher.process_text(amount, shift, 'ENCRYPT')

        return self._central_bank.withdraw_money(account_no, amount, shift)


class Manager(Employee):

    def __init__(self, username, password, permissions, central_bank):
        super().__init__(username, password, permissions, central_bank)

    def create_account(self, account_no, account_owner, starting_amount):
        # Encrypt the request data
        shift = randint(1, 67)
        account_no = caesar_cypher.process_text(account_no, shift, 'ENCRYPT')
        account_owner = caesar_cypher.process_text(account_owner, shift, 'ENCRYPT')
        starting_amount = caesar_cypher.process_text(starting_amount, shift, 'ENCRYPT')

        return self._central_bank.create_account(account_no, account_owner, starting_amount, shift)

    def delete_account(self, account_no):
        # Encrypt the request data
        shift = randint(1, 67)
        account_no = caesar_cypher.process_text(account_no, shift, 'ENCRYPT')

        return self._central_bank.delete_account(account_no, shift)

    def update_account(self, account_no, new_owner):
        # Encrypt the request data
        shift = randint(0, 67)
        account_no = caesar_cypher.process_text(account_no, shift, 'ENCRYPT')
        new_owner = caesar_cypher.process_text(new_owner, shift, 'ENCRYPT')

        return self._central_bank.update_account(account_no, new_owner, shift)
