class bike(object):
    def __init__(self, price, max_speed):
        self.price =  price
        self.max_speed = max_speed
        self.miles = 0
    def displayeinfo(self):
        print self.price
        print self.max_speed 
        print self.miles 
        return self
    def ride(self):
        self.miles=self.miles+10
        return self
    def reverse(self):
        self.miles=self.miles-5
        if self.miles < 0:
            self.miles = 0
        return self
    
bike1=bike(200,"300mph").displayeinfo().ride().reverse().displayeinfo()
bike2=bike(300,"200mph").ride().reverse().displayeinfo()
bike3=bike(2,"3mph").ride().reverse().displayeinfo()



# print bike1.price
# print bike1.max_speed
# print bike1.miles
# bike2=bike(20,"30mph")
# print bike2.price
# print bike2.max_speed
# print bike2.miles
# bike3=bike(2,"3mph")
# print bike3.price
# print bike3.max_speed
# print bike3.miles

