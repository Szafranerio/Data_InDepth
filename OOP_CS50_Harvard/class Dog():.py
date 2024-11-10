class Dog():
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def sit(self):
        print(f'{self.name.title()}, sits now')

    def roll(self):
        print(f'{self.name.title()}, rolls now')


my_dog = Dog('willie', 6, 'Poland')
your_dog = Dog('lucy', 5, 'Germany')

print(f'My dogs is {my_dog.name.title()} and has {my_dog.age} years old')

command = input('What is your command: ').strip().title()
if command == 'Sit':
   