class PaymentMethod:
    def process_payment(self, amount):
        raise NotImplementedError("Subclasses must implement this method.")
    

class CreditCard(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount} with 2% fee.")
        total = amount + (amount * 0.02)
        print(f"Total charged: ${total:.2f}\n")

class DebitCard(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing debit card payment of ${amount} with 1% fee.")
        total = amount + (amount * 0.01)
        print(f"Total charged: ${total:.2f}\n")

class PayPal(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount} with 3% fee.")
        total = amount + (amount * 0.03)
        print(f"Total charged: ${total:.2f}\n")

class CryptoCurrency(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing cryptocurrency payment of ${amount} with 0.5% fee.")
        total = amount + (amount * 0.005)
        print(f"Total charged: ${total:.2f}\n")

def process_transaction(payment_method, amount):
    payment_method.process_payment(amount)  # Polymorphism in action

# Main Program
if __name__ == "__main__":
    # Different payment methods
    credit_card = CreditCard()
    debit_card = DebitCard()
    paypal = PayPal()
    crypto = CryptoCurrency()

    # List of payments to process
    payments = [
        (credit_card, 1000),
        (debit_card, 500),
        (paypal, 750),
        (crypto, 1200)
    ]

    # Processing all transactions
    for payment_method, amount in payments:
        process_transaction(payment_method, amount)


