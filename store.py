class Store(object):
    def __init__(self,products,location,owner):
        self.products = products
        self.location = location
        self.owner = owner
    def add_product(self,product):
        self.products.append(product)
        return self
    def remove_product(self, product):
        self.products.remove(product)
        return self
    def inventory(self):
        print "Products:", self.products
        return self
    def store_info(self):
        print "Information:"
        print "Owner: " + str(self.owner)
        print "Location: " + str(self.location)
        return self
store1 = Store(["shirt","shoes","pants","hat"], "123 Coding Dojo Way, London, England", "The Queen")
store1.store_info()
store1.add_product("underwear").inventory()
store1.remove_product("shoes").inventory()
store1.add_product("necklace").remove_product("pants").store_info().inventory()