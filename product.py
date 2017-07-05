
class Product(object):
    def __init__(self, price, item_name, weight, brand, cost):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"

    def sell(self):
        self.status = "sold"
        return self

    def add_tax(self, tax):
        self.price = self.price + (self.price * tax)
        return self

    def rtrn(self, reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
        elif reason == "in box":
            self.status = "for sale"
        elif reason == "open box":
            self.status = "used"
            self.price = self.price - (self.price * .20)
        return self


steak = Product(10, "steak", "16oz", "Omaha", 2)
print steak.add_tax(0.08).price