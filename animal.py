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
    def displayHealth(self):
        print "Health: " + str(self.health)
        return self
animal1 = Animal("Harry", 50)
animal1.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name, 150)
    def pet(self):
        self.health += 5
        return self
dog1 = Dog("Fido")
dog1.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name, 170)
    def fly(self):
        self.health -= 10
        return self
    def displayHealth(self):
        super(Dragon, self).displayHealth()
        print "I am a Dragon"
dragon1 = Dragon("Bowzer")
dragon1.walk().fly().displayHealth()

class Bunny(Animal):
    def __init__(self, name, health):
        super(Bunny, self).__init__(name, health)

bunny1 = Bunny("Flopsy",50)
# bunny1.pet().displayHealth()
# bunny1.fly().displayHealth()
bunny1.walk().displayHealth()

# dog1.fly().displayHealth()