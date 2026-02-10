class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __eq__(self, other):
        return self.brand == other.brand and self.model == other.model

m1 = Mobile("Samsung", "S21", 50000)
m2 = Mobile("Samsung", "S21", 52000)
m3 = Mobile("Apple", "iPhone 13", 70000)

print(m1 == m2)
print(m1 == m3)
