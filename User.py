class User:
    def __init__(self, username, password, administrator, payment_method, bills):
        self.username = username
        self.password = password
        self.administrator = administrator
        self.payment_method = payment_method
        self.bills = bills

    def create_account(self, username, password):
        self.username = username
        self.password = password

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
