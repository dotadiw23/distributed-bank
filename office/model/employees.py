class Employee:

    def __init__(self, username, password, office, permissions):
        self.username = username
        self.password = password
        self.office = office
        self.permissions = permissions

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_office(self):
        return self.office

    def get_permissions(self):
        return self.permissions


class Cashier(Employee):

    def __init__(self, username, password, office, permissions):
        super().__init__(username, password, office, permissions)


class Manager(Employee):

    def __init__(self, username, password, office, permissions):
        super().__init__(username, password, office, permissions)
