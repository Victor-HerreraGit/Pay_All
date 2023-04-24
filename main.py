import datetime


class RegUsr:
    def __init__(self, usrName, passWrd):
        self.usrName = usrName
        self.passWrd = passWrd
        self.lastLogin = None

    def __str__(self):
        return f"Username: {self.usrName}, Password: {self.passWrd}, Last Login: {self.lastLogin}"


listAccountsRegUsr = [
    RegUsr("user1", "password1"),
    RegUsr("user2", "password2"),
    RegUsr("user3", "password3"),
    RegUsr("user4", "password4"),
    RegUsr("user5", "password5")
]


class admin:
    def __init__(self, usrName, passWrd):
        self.usrName = usrName
        self.passWrd = passWrd
        self.lastLogin = None

    def delete_inactive_account(self, username):
        for i, account in enumerate(listAccountsRegUsr):
            if account.usrName == username:
                if (datetime.datetime.now() - account.lastLogin).days > 90:
                    listAccountsRegUsr.pop(i)
                    print(f"Regular user account '{username}' successfully deleted")
                else:
                    print("Account is still active within the last 90 days")
                return listAccountsRegUsr
        print("Account does not exist")
        return listAccountsRegUsr

    def announce(self, message, importance=0):
        if message == "":
            print("Error: Empty message")
        elif len(message) > 50:
            print("Error: Message is too long")
        else:
            if importance == 1:
                print("IMPORTANT:", message)
            else:
                print(message)

    def login(self):
        # Set the lastLogin attribute to the current date and time
        self.lastLogin = datetime.datetime.now()


# Create three dummy lastLogin dates in the past (Boundary Test Cases)
lastLogin1 = datetime.datetime.now() - datetime.timedelta(days=89)
lastLogin2 = datetime.datetime.now() - datetime.timedelta(days=90)
lastLogin3 = datetime.datetime.now() - datetime.timedelta(days=91)

# Set the lastLogin attribute of the RegUsr objects in the listAccountsRegUsr list to the dummy dates
listAccountsRegUsr[0].lastLogin = lastLogin1
listAccountsRegUsr[1].lastLogin = lastLogin2
listAccountsRegUsr[2].lastLogin = lastLogin3

# Create a new admin account and set its lastLogin attribute to the current date and time
admin1 = admin("admin1", "admin-password1")
admin1.login()

# METHOD delete_inactive
# Test the delete_inactive_account method
account_to_delete_89_Days = "user1"
account_to_delete_90_Days = "user2"
account_to_delete_91_Days = "user3"

# 3 Boundary Test Cases
print("###Test Cases for delete_inactive_account method###")
print("Test Case 1 for delete_inactive_account method")
admin1.delete_inactive_account(account_to_delete_89_Days)
print("\nTest Case 2 for delete_inactive_account method")
admin1.delete_inactive_account(account_to_delete_90_Days)
print("\nTest Case 3 for delete_inactive_account method")
admin1.delete_inactive_account(account_to_delete_91_Days)
print("\nRemaining users")
for account in listAccountsRegUsr:
    print(account.usrName)

# METHOD announce
# Test Case 1: Default importance level
print("\n###Test Cases for announce method###")
print("Test Case 1 for announce method")
admin1.announce("This is a regular announcement")
# Test Case 2: High importance level
print("\nTest Case 2 for announce method")
admin1.announce("This is an important announcement", 1)
# Test Case 3: Empty message
print("\nTest Case 3 for announce method")
# Test Case 3: Empty message
admin1.announce("")
print("\nTest Case 4 for announce method")
# Test Case 4: Message length less than 50 characters
admin1.announce("This is a regular announcement")
print("\nTest Case 5 for announce method")
# Test Case 5: Message length exactly 50 characters
admin1.announce("A message with exactly 50 characters only.12345")
print("\nTest Case 6 for announce method")
# Test Case 6: Message length more than 50 characters
admin1.announce("A message with more than 50asdfafasdfasgasdgakjsdgkjhgjkahgkjhakghajksdgha")


# End