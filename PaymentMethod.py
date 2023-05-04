class PaymentMethod:
  def __init__(self, name, typ, expirationYear, number, securityCode, routingNumber):
    self.name = name
    self.typ = typ
    self.expiration = expirationYear
    self.number = number
    self.securityCode = securityCode
    self.routingNumber = routingNumber

def addPaymentMethod(user, name, typ, expirationYear, number, securityCode, routingNumber):
    global PaymentMethods
    if not (typ == "Debit" or typ == "Credit"):
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

    user.PaymentMethods.append(PaymentMethod(name, typ, expirationYear, number, securityCode, routingNumber))
    print("Payment method: ", name, " added")
    

def deletePaymentMethod(user, Payment):
    if(Payment == None):
        print(Payment, " Invalid")

    user.PaymentMethods.remove(Payment)
    print("Payment method: ", Payment.name, " removed")
    
# if __name__ == "__main__":
#     print(len(PaymentMethods))
#     addPaymentMethod("Hello", "Credit", 2024, "1111111111111111", "868", "000000000")
#     print(len(PaymentMethods))
#     deletePaymentMethod(PaymentMethods[0])
#     print(len(PaymentMethods))