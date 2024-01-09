# Target Interface
class DollarPaymentProcessor:
    def process_payment(self, dollars):
        print(f"Processing ${dollars} payment.")

# Adaptee
class EuroPayment:
    def pay_in_euros(self, euros):
        print(f"Paying €{euros} in euros.")

# Adapter
class EuroToDollarAdapter(DollarPaymentProcessor):
    def __init__(self, euro_payment):
        self.euro_payment = euro_payment

    def process_payment(self, dollars):
        euros = dollars * 0.85  # Assuming 1 dollar = 0.85 euros
        self.euro_payment.pay_in_euros(euros)

# Usage
euro_payment = EuroPayment()
adapter = EuroToDollarAdapter(euro_payment)
adapter.process_payment(100)  # $100
