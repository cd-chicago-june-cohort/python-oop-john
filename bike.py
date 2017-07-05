class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    
    def displayInfo(self):
        string = "Price: {}, Max speed: {}, Total miles: {}".format(self.price, self.max_speed, self.miles)
        return string

    def ride(self):
        print "Riding"
        self.miles += 10
        return self

    def reverse(self):
        print "Reversing"
        self.miles -= 5
        return self



bike1 = Bike(200, "25mph")
print bike1.ride().ride().ride().reverse().displayInfo()

print "-" * 50

bike2 = Bike(400, "30mph")
print bike2.ride().ride().reverse().reverse().displayInfo()

print "-" * 50

bike3 = Bike(300, "20mph")
print bike2.reverse().reverse().reverse().displayInfo()
