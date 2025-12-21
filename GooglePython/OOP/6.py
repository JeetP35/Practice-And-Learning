class Fruit:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

class SomeApple(Fruit):
    pass

class SomeGrape(Fruit):
    pass

granny_smith = SomeApple("green", "tart")
carnelian = SomeGrape("purple", "sweet")
print(granny_smith.flavor)
print(granny_smith.color)
print(carnelian.flavor)
print(carnelian.color)


class Animal:
    sound = ""
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("{sound} I'm {name}! {sound}".format(name=self.name, sound=self.sound))

class Dog(Animal):
    sound = "Woof"
doggy = Dog("Dogesh")
doggy.speak()

class Cat(Animal):
    sound = "Meow"
catty = Cat("Catrina")
catty.speak()