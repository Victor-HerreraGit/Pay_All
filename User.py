class User:
    def __init__(self, username, password, administrator, payment_method, bills):
        self.username = username
        self.password = password
        self.administrator = administrator
        self.payment_method = payment_method
        self.bills = bills

    def __str__(self):
        return f"Username: {self.username}, Administrator: {self.administrator},Payment Method: {self.payment_method}, Bill: {self.bills}"

    def create_account(self, username, password):
        if username is None or password is None:
            raise ValueError("Username and password cannot be None.")
            return
        self.username = username
        self.password = password
        print("Account Created")

    def modify_account(self, username=None, password=None, administrator=None, payment_method=None, bills=None):
        if username:
            self.username = username
        if password:
            self.password = password
        if administrator is not None:
            self.administrator = administrator
        if payment_method:
            self.payment_method = payment_method
        if bills:
            self.bills = bills

    def delete_account(self):
        self.username = None
        self.password = None
        self.administrator = None
        self.payment_method = None
        self.bills = None


# Test
user1 = User('Victor', "verification", False, "Fed Now", 50.0)
user1.modify_account(None, None, None, None, None)
print(user1.username)
# print(f" User name: {user1.username},\n Current Password: {user1.password},\n current balance on bill: {user1.bills}")
# print()
