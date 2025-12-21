class Piglet:
    name = "Piglet"
    def speak(self):
        print("Oink! I'm {}. Oink!".format(self.name))        
    
piggy = Piglet()
piggy.name = "Porky"
piggy.speak()

spider = Piglet()
spider.name = "Peter Porker"
spider.speak()