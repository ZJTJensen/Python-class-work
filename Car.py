class car(object):
    def __init__(self,price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self. fuel = fuel
        self. mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else: 
            self.tax = 0.12
    def display_all(self):
        print self.price
        print self.speed
        print self.fuel
        print self.mileage
        print self.tax
        return self


car1 = car(2000, "60mph", "full", "20mpg").display_all()
car2 = car(20000, "60mph", "full", "20mpg").display_all()
car3 = car(20000, "60mph", "full", "20mpg").display_all()
car4 = car(20000, "60mph", "full", "20mpg").display_all()
car5 = car(2000, "60mph", "full", "20mpg").display_all()
car6 = car(2000, "60mph", "full", "20mpg").display_all()
