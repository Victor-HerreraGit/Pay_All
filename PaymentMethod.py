class PaymentMethod:
  def __init__(self, name, type, expirationYear, number, securityCode, routingNumber):
    self.name = name
    self.type = type
    self.expiration = expirationYear
    self.number = number
    self.securityCode = securityCode
    self.routingNumber = routingNumber

PaymentMethods = []

def addPaymentMethod(name, type, expirationYear, number, securityCode, routingNumber):
    global PaymentMethods
    if not (type == "Debit" or type == "Credit"):
        print("Invalid Input: Please input either Debit or Credit")
        return

    if(expirationYear > 3000):
        print("Invalid Year: Please input valid year")
        return

    if(len(number) != 16):
        print("Invalid card number: Please input valid number")
        return

    if(len(securityCode) != 3):
        print("Invalid securityCode: Please input valid code")
        return

    if(len(routingNumber) != 9):
        print("Invalid routing number: Please input valid routing number")
        return

    PaymentMethods.append(PaymentMethod(name, type, expirationYear, number, securityCode, routingNumber))
    print("Payment method: ", name, " added")
    

def deletePaymentMethod(Payment):
    if(Payment == None):
        print(Payment, " Invalid")

    PaymentMethods.remove(Payment)
    print("Payment method: ", Payment.name, " removed")

print(len(PaymentMethods))
addPaymentMethod("Hello", "Credit", 2024, "1111111111111111", "868", "000000000")
print(len(PaymentMethods))
deletePaymentMethod(PaymentMethods[0])
print(len(PaymentMethods))