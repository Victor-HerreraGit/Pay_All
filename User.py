class User:
    def __init__(self, username, password, administrator, payment_methods = [], bills = []):
        self.username = username
        self.password = password
        self.administrator = administrator
        self.payment_methods = payment_methods
        self.bills = bills
        self.billing_accounts = []
        
    def __str__(self):
        methods = ""
        for method in self.payment_methods.values():
            methods = methods + "\n" + str(method)
            
        billsStr = ""
        for bill in self.bills.values():
            billsStr = billsStr + "\n" + str(bill)
        return f"Username: {self.username}\nAdministrator: {self.administrator}\nPayment Method: {methods}\nBill: {billsStr}"

    def create_account(self, username, password):
        if username is None or password is None:
            raise ValueError("Username and password cannot be None.")
            return
        self.username = username
        self.password = password
        print("Account Created")

    def add_Bill(self, bill):
        if bill is None:
            raise ValueError("Bill cannot be None.")
            return
        if bill in self.bills:
            print("Bill already linked to User")
            return
        self.bills.append(bill)
        print("Bill added")

    def modify_account(self, username=None, password=None, administrator=None, payment_methods=None, bills=None):
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if administrator is not None:
            self.administrator = administrator
        if payment_methods is not None:
            self.payment_methods = payment_methods
        if bills is not None:
            self.bills = bills

    def delete_account(self):
        self.username = None
        self.password = None
        self.administrator = None
        self.payment_method = None
        self.bills = None


# Test
if __name__ == "__main__":
    user1 = User('Victor', "verification", False, "Fed Now", 50.0)
    user1.modify_account(None,None,None,None,None)
    print(user1.username)
    # print(f" User name: {user1.username},\n Current Password: {user1.password},\n current balance on bill: {user1.bills}")
    # print("", user1.payment_method)
