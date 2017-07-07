class Product(object):
    def __init__(self, price, name, weight, brand, cost):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"
    def sell(self):
        self.status = "sold"
        return self
    def add_tax(self,tax):
        self.price += self.price * tax
        return self
    def returns(self, reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
            return self
        elif reason == "in box":
            self.status = "for sale"
            return self
        elif reason == "opened":
            self.status = "used"
            self.price -= self.price * 0.2
            return self
    def display_info(self):
        print "Price: $" + str(self.price)
        print "Name: " + str(self.name)
        print "Weight: " + str(self.weight) + " lbs"
        print "Brand: " + str(self.brand)
        print "Cost: $" + str(self.cost)
        print "Status: " + str(self.status)

shirt = Product(30, "t-shirt", 2, "Zara", 30)
shirt.add_tax(.15).sell().display_info()
pants = Product(50, "jeans", 2, "Levi", 50)
pants.add_tax(.20).sell().returns("defective").display_info()
hat = Product(25, "hat", 2, "Life's Good", 25)
hat.add_tax(.10).sell().returns("opened").display_info()