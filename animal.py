class Animal(object):
    def __init__(self, name, health):
        self.name=name
        self.health=health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print self.health
        return self

# animal1 = Animal("ardvark", 100).walk().walk().walk().run().run().display_health()

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name, 150)
    def pet(self):
        self.health += 5
        return self

Dog1 = Dog("good boy").walk().walk().walk().walk().walk().run().run().pet().pet().display_health()

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name, 170)
    def fly(self):
        self.health -=5
        return self
    def display_health(self):
        print "I am a dragon"
        print self.health
        return self

# Dragon1 = Dragon("Drogon").display_health()