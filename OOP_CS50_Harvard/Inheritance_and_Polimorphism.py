class Animal():
    
    def __init__(self):
        print('Animal created')
        
    def who_am_i(self):
        print('I am an animal')
        
    def eat(self):
        print('I am eating')
        
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog created')
    
    def bark(self):
        print('Woof')
        
my_dog = Dog()
my_dog.eat()
my_dog.bark()

#Polimorphism

class Dog():
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        return self.name + ' says woof!'
    
class Cat():
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        return self.name + ' says moew!'
    
niko = Dog('Niko')
rollo = Cat('Rollo')

print(niko.speak())
print(rollo.speak())
    
for pet in [niko,rollo]:
    print(type(pet))
    print(pet.speak())
    
def pet_speak(pet):
    print(pet.speak())
    
pet_speak(rollo)