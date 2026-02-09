class Payment:
    def pay(self):
        print("Making a payment")

class GooglePay(Payment):
    def pay(self):
        print("Payment made using Google Pay")

class PhonePe(Payment):
    def pay(self):
        print("Payment made using PhonePe")

class CreditCard(Payment):
    def pay(self):
        print("Payment made using Credit Card")

p = Payment()
g = GooglePay()
ph = PhonePe()
c = CreditCard()

p.pay()
g.pay()
ph.pay()
c.pay()

