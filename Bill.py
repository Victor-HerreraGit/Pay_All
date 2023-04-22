class Bill:
    def __init__(self, user, payment_method):
        self.user = user
        self.payment_method = payment_method
        self.billing_accounts = []
        self.payment_history = []