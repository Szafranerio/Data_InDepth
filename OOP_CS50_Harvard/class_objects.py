class Dog():
    
    #CLASS OBJECT ATRIBUTE - same for all, no need for self
    species = 'mammal'
    
    def __init__(self,name,breed,spots):
        self.name = name
        self.breed = breed
        self.spots = spots
    
    #Operation/Actions ---> Method
    def bark(self, number):
        print('Woof, My name is {} and the number is {}'.format(self.name, number))
        
my_dog = Dog('Azor', 'Labrador', 'No')
print(my_dog.species)
my_dog.bark(7)

class Circle():
    
    #Class object
    pi = 3.14
    
    def __init__(self, radius=1):
        self.radius = radius
        
    def math(self):
        return self.radius * self.pi * 2
    
circle = Circle(65)
print(circle.math())