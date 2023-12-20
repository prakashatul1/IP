# Strategy Interface
class PaymentMethod:
    def pay(self, amount):
        pass

# Concrete Strategies
class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paying ${amount} using Credit Card.")

class PayPalPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paying ${amount} using PayPal.")

class BitcoinPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paying ${amount} using Bitcoin.")

# Context
class PaymentProcessor:
    def __init__(self, payment_method):
        self.payment_method = payment_method

    def process_payment(self, amount):
        self.payment_method.pay(amount)

# Usage
payment_processor = PaymentProcessor(CreditCardPayment())
payment_processor.process_payment(100)
