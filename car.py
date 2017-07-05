
class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = "12%"
        if price > 10000:
            self.tax = "15%"
        print self.display_all()

    def display_all(self):
        string = "Price: {} \nSpeed: {} \nFuel: {} \nMileage: {} \nTax: {}".format(self.price, self.speed, self.fuel, self.mileage, self.tax)
        return string
    
    
car1 = Car(20000, "30mph", "Full", "40mpg")
print "-" * 50
car2 = Car(10000, "55ph", "Not full", "30mpg")
print "-" * 50
car3 = Car(4000, "70mph", "Full", "22mpg")
print "-" * 50
car4 = Car(7000, "15mph", "Not full", "38mpg")
print "-" * 50
car5 = Car(1000, "20mph", "Full", "44mpg")
print "-" * 50
car6 = Car(17000, "90mph", "Not full", "18mpg")