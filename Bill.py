import random

from PaymentMethod import PaymentMethod
from User import User

import datetime
class Bill:
    def __init__(self, user, amount, account):
        self.user = user
        self.full_amount = amount
        self.unpaid_amount = amount
        self.billing_account = account
        self.payment_history = []

    def __str__(self):
        return f"Bill for {self.user.username}\n\tOriginal Amount: {self.full_amount}\n\tUnpaid Balance: {self.unpaid_amount}\n\tBilling Account: {self.billing_account.name}\n\tPayment History: {self.payment_history}"

    def pay_bill(self, amount, payment_method):
        
        if amount <= 0:
            print("Error: Invalid payment amount")
            return
        
        if amount > self.unpaid_amount:
            print("Error: Invalid payment amount, amount to pay cannot be greater than the owed amount")
            return 
        
        if payment_method is None:
            print("Error: Payment method invalid")
            return

        payment = {
            "billing_account": self.billing_account,
            "payment_method": payment_method,
            "payment_amount": amount,
            "payment_date": datetime.datetime.now()
        }

        self.payment_history.append(payment)
        self.billing_account.payment_history.append(payment)
        
        self.unpaid_amount = round(self.unpaid_amount - amount, 2)

        print(f"Payment of {payment['payment_amount']} made on {payment['payment_date']} for billing account {payment['billing_account']} using payment method {payment['payment_method']}")
        reply = input("Would you like to set up recurring payments for this bill? Y/N")

        if reply.lower() == "y":
            self.billing_account.setUpRecurringPayments(amount, payment_method)

class BillingAccount:
    def __init__(self, name, user):
        self.name = name
        self.user = user
        self.api_endpoint = ""
        self.payment_history = []
        self.recurring_payments = []
        self.frequency = 30 
        # 30 days for recurring payments
        self.bills = []
        
    def __str__(self):
        string = self.name + '\n\tRecurring Payments:'
        for recur in self.recurring_payments:
            string = string + "\n\t" + str(recur)
        return string
        
    def getBills(self, paid = False):
        #return bills associated with class
        if paid:
            return self.bills
        else:
            unpaid_bills = []
            for bill in self.bills:
                if bill.unpaid_amount > 0:
                    unpaid_bills.append(bill)
            return unpaid_bills
    
    def queryBills(self, user):
        #generate a bill for testing #FIXME mockup
        bill = Bill(user, round(random.uniform(0.01, 100.00), 2), self)
        self.bills.append(bill)
        return "New Bill: " + str(bill)
    
    def viewPaymentHistory(self):
        if self.payment_history is None or len(self.payment_history) < 1:
            print("No payments made yet")
        else:
            for payment in self.payment_history:
                print("Payment History for Billing Account:", payment["billing_account"])
                print("Payment Date:", payment["payment_date"])
                print("Payment Method:", payment["payment_method"])
                print("Amount: $", payment["payment_amount"], sep="")
                
    def setUpRecurringPayments(self, amount, payment_method, frequency = None):
        if frequency == None:
            frequency = self.frequency

        amount = round(amount, 2) # make sure in 1/100ths not fractional cents
        if payment_method is None:
            print("Error: No payment method available")
            reply = input("Would you like to add a payment method now? Y/N")
            if reply == "Y":
                name = input("Name: ")
                typ = input("Type: ")
                expYear = input("Expiration Year: ")
                num = input("Card Number: ")
                code = input("Security Code: ")
                route = input("Routing: ")
                payment_method = self.payment_method.addPaymentMethod(name, typ, expYear, num, code, route)

            else:
                print("Error: No Payment Method Found")
                return

        if amount <= 0:
            print("Error: Invalid bill amount")
            return

        recurring_payment = {
            "billing_account": self,
            "payment_method": payment_method,
            "bill_amount": amount,
            "last_payment_date": datetime.datetime.now(),
            "frequency": frequency
        }

        self.recurring_payments.append(recurring_payment)

        print(f"Recurring payment set up for billing account: {recurring_payment['billing_account']}, payment method: {recurring_payment['payment_method']}, in the amount of: {recurring_payment['bill_amount']}.")

    def linkBillingAccount(user, billing_account):
        if billing_account in user.billing_accounts:
            print("Error: Billing account is already linked")
            return
        
        user.billing_accounts.append(billing_account)
        print(f"Billing account {billing_account} linked successfully")

def deleteBillingAccount(user, bill_acct_name):
    if not bill_acct_name in user.billing_accounts:
        return "No matching Billing accounts"
    
    user.billing_accounts.pop(bill_acct_name, None)
    return "Billing account deleted"

def addBillingAccount(user, bill_acct_name):
    if bill_acct_name in user.billing_accounts:
        return "Billing account {} NOT added, perhaps there is an account with that name already?".format(bill_acct_name)
    user.billing_accounts[bill_acct_name] = BillingAccount(bill_acct_name, user)
    return "Billing account {} added".format(bill_acct_name)

if __name__ == "__main__":
    # Test
    user = User("Victor", "verification", False, "Fed Now", 50.0)
    bill = Bill(user, 100, "netflix")
    bill.setUpRecurringPayments(100, "netflix", "visa")
    # payment = {
    #             "billing_account": "test",  
    #             "payment_method": "visa",
    #             "payment_amount": 50,
    #             "payment_date": "11:59"
    #         }
    # payment2 = {
    #             "billing_account": "test",  
    #             "payment_method": "visa",
    #             "payment_amount": 50,
    #             "payment_date": "11:59"
    #         }
    # bill.payment_history.append(payment)
    # bill.payment_history.append(payment2)
    # bill.viewPaymentHistory()