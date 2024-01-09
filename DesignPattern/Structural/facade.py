# Complex Systems
class Authorization:
    def authorize(self):
        print("Authorization complete.")

class CurrencyConverter:
    def convert(self, amount):
        print(f"Converted amount: ${amount}")
        return amount

class PaymentProcessor:
    def process(self, amount):
        print(f"Processed payment of ${amount}")

# Facade
class PaymentServiceFacade:
    def __init__(self):
        self.authorizer = Authorization()
        self.converter = CurrencyConverter()
        self.processor = PaymentProcessor()

    def make_payment(self, amount):
        self.authorizer.authorize()
        converted_amount = self.converter.convert(amount)
        self.processor.process(converted_amount)

# Usage
payment_service = PaymentServiceFacade()
payment_service.make_payment(100)
