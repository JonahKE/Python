class Car(object):
    def __init__(self,price,speed,fuel,mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = "15%"
        else:
            self.tax = "12%"
        def display_all():
            print "Price: " + str(self.price) 
            print "Speed: " + str(self.speed)
            print "Fuel: " + str(self.fuel)
            print "Mileage: " + str(self.mileage)
            print "Tax: " + str(self.tax)
        display_all()
one = Car(2000,"35mph","Full","15mpg")
one