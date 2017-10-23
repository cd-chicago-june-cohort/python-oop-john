

class Store(object):
    def __init__(self, location, owner):
        self.products = []
        self.location = location
        self.owner = owner

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        for i in range(len(self.products)):
            if self.products[i] == product:
                self.products.pop(i)
                return;

    def inventory(self):
        for p in self.products:
            print(p);



Galleria = Store("River North", "some guy")

Galleria.add_product("Italian Supreme")
Galleria.add_product("Gum")
Galleria.add_product("Steaz")
Galleria.add_product("Sausage, egg, and cheese")

Galleria.inventory()

Galleria.remove_product("Gum")

Galleria.inventory()