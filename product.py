class product(object):
    def __init__(self, price, item_name, weight, brand, status):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = status
    def sell(self):
        self.status= "sold"
        return self
    def add_tax(self):
        self.tax = 0.06
        self.price = self.price + self.tax
        return self
    def reason_return(self, note):            
        if note== 1:
            self.status= "used"
            self.price =self.price- (self.price* 0.20)
            return self
        if note== "defective":
            self.status = "defective"
            self.price = 0
            return self
    def displayinfo(self):
       print self.price
       print self.item_name
       print self.weight 
       print self.brand 
       print self.status 
       return self

product1 = product(10.00, "toy", "2lbs", "nike", "stuff").reason_return(1).displayinfo()