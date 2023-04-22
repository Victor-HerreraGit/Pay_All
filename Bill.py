class Bill:
    def __init__(self, user, payment_method):
        self.user = user
        self.payment_method = payment_method
        self.billing_accounts = []
        self.payment_history = []

    def view_bills(self):
        pass

    def setUpRecurringPayments(self):
        pass

    def linkBillingAccount(self):
        pass

    def deleteBillingAccount(self):
        pass

    def addBillingAccount(self):
        pass

    def pay_bill(self):
        pass

    def viewPaymentHistory(self):
        pass