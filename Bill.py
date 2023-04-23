import datetime
class Bill:
    def __init__(self, user, payment_method, amount):
        self.user = user
        self.payment_method = payment_method
        self.amount = amount
        self.billing_accounts = []
        self.payment_history = []
        self.recurring_payments = {}
        self.frequency = 30 
        # 30 days for recurring payments

    def view_bills(self):
        pass

    def setUpRecurringPayments(self, amount, billing_account):

        payment_method = self.payment_method
        frequency = self.frequency

        if payment_method is None:
            print("Error: No payment method available")
            return

        if billing_account not in self.billing_accounts:
            print("Error: Billing account not found")
            return 

        if amount <= 0:
            print("Error: Invalid bill amount")
            return

        recurring_payment = {
            "billing_account": billing_account,
            "payment_method": payment_method,
            "bill_amount": amount,
            "last_payment_date": datetime.now().date()
        }

        self.recurring_payments.append(recurring_payment)
        self.payment_history.append(recurring_payment)

        print(f"Recurring payment set up for billing account: {self.recurring_payments['billing_account']}, payment method: {self.recurring_payments['payment_method']}, in the amount of: {self.recurring_payments['bill_amount']}. Your last payment was made on: {self.recurring_payments['last_payment_date']}.")


    def linkBillingAccount(self):
        pass

    def deleteBillingAccount(self):
        pass

    def addBillingAccount(self):
        pass

    def pay_bill(self, amount, billing_account):
        
        if amount <= 0:
            print("Error: Invalid payment amount")
            return

        if billing_account not in self.billing_accounts:
            print("Error: Billing account not found")
            return 

        if self.payment_method is None:
            print("Error: No payment method available")
            return

        payment = {
            "billing_account": billing_account,  
            "payment_method": self.payment_method,
            "payment_amount": amount,
            "payment_date": datetime.now().date()
        }

        self.payment_history.append(payment)

        print(f"Payment of {payment['payment_amount']} made on {payment['payment_date']} for billing account {payment['billing_account']} using payment method {payment['payment_method']}")

    def viewPaymentHistory(self):
        pass