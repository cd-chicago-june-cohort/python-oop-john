class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print self.health
        return self

# cat = Animal("cat", 100)
# cat.walk().walk().walk().run().run().display_health()





class Dog(Animal):
    def __init__(self, name, health):
        super(Dog, self).__init__(name, health)
        self.health = 150
    
    def pet(self):
        self.health += 5
        return self

Chuck = Dog("Chuck", 200)
# Chuck.walk().walk().walk().run().run().pet().display_health()





class Dragon(Animal):
    def __init__(self, name, health):
        super(Dragon, self).__init__(name, health)
        self.health = 170
    
    def fly(self):
        self.health -= 10
        return self

    def display_health(self):
        super(Dragon, self).display_health()
        print "I am a dragon"
        return self

# my_dragon = Dragon("My Dragon", 300)
# my_dragon.fly().display_health()





lion = Animal("lion", 500)
#lion.pet().display_health()
#Chuck.fly()