from abc import ABC, abstractmethod

class Order:
    items = []
    quantities = []
    prices = []
    status = "open"  # payment status

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
       total = 0
       for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
       return total

class Authorizer(ABC):
    @abstractmethod
    def is_authorized(self) -> bool:
        pass

class SMSAuth(Authorizer):

    authorized = False

    def verify_code(self, code):
        print(f"Verifying code {code}")
        self.authorized= True

    def is_authorized(self) -> bool:
        return self.authorized

class NotARobot(Authorizer):
    authorized = False

    def not_a_robot(self):
        print("Are you a robot? Naaaaa...")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized

class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order):
        pass


class DebitPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code, authorizer: Authorizer):
        self.authorizer = authorizer
        self.security_code = security_code

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

class CreditPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

class PaypalPaymentProcessor(PaymentProcessor):

    def __init__(self, email_address, authorizer: Authorizer):
        self.authorizer = authorizer
        self.email_address = email_address

    def auth_sms(self, code):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing paypal payment type")
        print(f"Using email_address: {self.email_address}")
        order.status = "paid"

order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
authorizer = NotARobot()
processor = DebitPaymentProcessor("2349875", authorizer)
authorizer.not_a_robot()
processor.pay(order)
