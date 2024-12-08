class Animal():
    def __init__(self, species):
        if not isinstance (species,str) or not species.strip():
            raise ValueError ("\033[91m[Error]\033[0m - Must be a string")
        self.species = species
               
class Bird(Animal):
    def __init__(self, species):
        super().__init__(species)
        
class Reptile(Animal):
    def __init__(self, species):
        super().__init__(species)

try:        
    bird = Bird("")
    print(f'{bird.species}')
except ValueError as error:
    print(error)

try:  
    lizard = Reptile("Tom")
    print(f'{lizard.species}')
except ValueError as error:
    print(