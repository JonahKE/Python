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
        self.display_all()
    def display_all(self):
        print "Price: " + str(self.price) 
        print "Speed: " + str(self.speed)
        print "Fuel: " + str(self.fuel)
        print "Mileage: " + str(self.mileage)
        print "Tax: " + str(self.tax)
one = Car(2000,"35mph","Full","15mpg")
one
two = Car(2000,"5mph","Not Full","105mpg")
two
three = Car(2000,"15mph","Kind of Full","95mpg")
three
four = Car(2000,"25mph","Full","25mpg")
four
five = Car(2000,"45mph","Empty","25mpg")
five
six = Car(20000000,"35mph","Empyty","15mpg")
six