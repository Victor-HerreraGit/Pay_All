class PaymentMethod:
    def __init__(self, name, typ, expirationYear, number, securityCode, routingNumber):
        self.name = name
        self.typ = typ
        self.expiration = expirationYear
        self.number = number
        self.securityCode = securityCode
        self.routingNumber = routingNumber
    
    def __str__(self):
        return f"Payment Method {self.name}, type: {self.typ}, exp: {self.expiration}, num: {self.number}, CVV: {self.securityCode}, routing: {self.routingNumber}"
    
def addPaymentMethod(user, name, typ, expirationYear, number, securityCode, routingNumber):
    if valType(typ) and valExp(expirationYear) and valNum(number) and valSecCode(securityCode) and valRouteNum(routingNumber):
        user.payment_methods[name] = (PaymentMethod(name, typ, expirationYear, number, securityCode, routingNumber))
        print("Payment method: ", name, " added")

def valName(user, name): #check for user already having payment method of that name
    if name in user.payment_methods:
        print("Method name already taken")
        return False
    return True

def valType(typ):
    typ = typ.lower()
    if not (typ == "debit" or typ == "credit"):
        print("Invalid Input: Please input either Debit or Credit")
        return False
    return True

def valExp(exp):
    try:
        int(exp)
    except TypeError:
        print("Cannot interpret input as year/integer")
        return False
    if(int(exp) > 3000):
        print("Invalid Year: Please input valid year")
        return False
    return True

def valNum(num):
    if(len(num) != 16):
        print("Invalid card number: Please input valid number")
        return False
    return True

def valSecCode(code):
    if(len(code) != 3):
        print("Invalid securityCode: Please input valid code")
        return False
    return True

def valRouteNum(routenum):
    if(len(routenum) != 9):
        print("Invalid routing number: Please input valid routing number")
        return False
    return True

def deletePaymentMethod(user, Payment):
    if(Payment == None):
        print(Payment, " Invalid")

    user.payment_methods.pop(Payment, None)
    print("Payment method: ", Payment, " removed")
    
# if __name__ == "__main__":
#     print(len(PaymentMethods))
#     addPaymentMethod("Hello", "Credit", 2024, "1111111111111111", "868", "000000000")
#     print(len(PaymentMethods))
#     deletePaymentMethod(PaymentMethods[0])
#     print(len(PaymentMethods))