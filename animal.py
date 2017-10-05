class animal(object):
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
        print "Current Health:", self.health
        return self

animal1 = animal('TheOne', 200)
animal1.walk().walk().walk().run().run().displayHealth()

class dog(animal):
    def __init__(self, name):
        super(dog, self).__init__(self, name)
        self.health = 150
    def pet(self):
        self.health += 5
        return self

dog1 = dog('Doggy')
dog1.walk().walk().walk().run().run().pet().displayHealth()

class dragon(animal):
    def __init__(self, name):
        super(dragon, self).__init__(self, name)
        self.health = 170
    def fly(self):
        self.health -= 10
        return self
    def displayHealth(self):
        print 'I am a Dragon', self.health
        return self

dragon1 = dragon('DRAGOON')
dragon1.fly().displayHealth()

#Check Tests

animal2 = animal('test', 300)
#animal2.fly().displayHealth()           

dog2 = dog('test1')
#dog2.fly().displayHealth()