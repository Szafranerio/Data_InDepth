class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.range = 0

    def get_descriptive(self):
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()

    def read_range(self):
        print(f'The range of car is {self.range} km')

    def update_range(self, new_range):
        self.range = new_ran