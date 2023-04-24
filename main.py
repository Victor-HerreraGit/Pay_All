import datetime

listAccountsRegUsr = ["bluebird", "firefly11", "greenapple", "sunnydayz", "watermelon7"]


class RegUsr:
    def __init__(self, usrName, passWrd):
        self.usrName = usrName
        self.passWrd = passWrd
        self.lastLogin = None


class admin:
    def __init__(self, usrName, passWrd):
        self.usrName = usrName
        self.passWrd = passWrd
        self.lastLogin = None

    def delete_inactive_account(self, account):
        if isinstance(account, RegUsr) and (datetime.datetime.now() - account.lastLogin).days > 90:
            listAccountsRegUsr.remove(account)
            print(f"Regular user account '{account.usrName}' successfully deleted")
        else:
            print("Invalid account or account has been active within the last 90 days")
        return listAccountsRegUsr

    def announce(self, message):
        print(message)

    def login(self):
        # Set the lastLogin attribute to the current date and time
        self.lastLogin = datetime.datetime.now()


# Create three dummy lastLogin dates in the past
lastLogin1 = datetime.datetime.now() - datetime.timedelta(days=100)
lastLogin2 = datetime.datetime.now() - datetime.timedelta(days=60)
lastLogin3 = datetime.datetime.now() - datetime.timedelta(days=30)

# Create three new regular user accounts and set their lastLogin attribute to the dummy dates
account1 = RegUsr("user1", "password1")
account1.lastLogin = lastLogin1

account2 = RegUsr("user2", "password2")
account2.lastLogin = lastLogin2

account3 = RegUsr("user3", "password3")
account3.lastLogin = lastLogin3

# Create a new admin account and set its lastLogin attribute to the current date and time
admin1 = admin("admin1", "admin-password1")
admin1.login()

# Test the delete_inactive_account method
account_to_delete = account1
admin1.delete_inactive_account(account_to_delete)

# Print the list of remaining regular user accounts
print(listAccountsRegUsr)
