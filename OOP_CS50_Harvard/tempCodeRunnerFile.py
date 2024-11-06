class Animal:
    def speak(self):
        print("This animal makes a sound.")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

# Testing polymorphism
animals = [Dog(), Cat()]
for animal in animals:
    animal.speak()