import Pyro4

# Pyro setup
ns = Pyro4.locateNS()
uri = ns.lookup('central_bank')
central_bank = Pyro4.Proxy(uri)

def update_account_state(account1, account2):
    central_bank.update_account_state(account1, account2)