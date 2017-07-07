class Bike(object):
    def __init__(self,price,max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print 'The price is: $' + str(self.price)
        print 'Max speed: ' + str(self.max_speed)
        print 'Total miles: ' + str(self.miles)
    def ride(self):
        print "Riding"
        self.miles += 10
        return self
    def reverse(self):
        #prevent negative miles
        if self.miles >= 5:
            print "Reversing"
            self.miles -= 5
        return self
first = Bike(200, "25mph")
first.ride().ride().ride().reverse().displayInfo()
second = Bike(100, "15mph")
second.ride().ride().reverse().reverse().displayInfo()
third = Bike(50, "10mph")
second.ride().reverse().reverse().reverse().reverse().displayInfo()