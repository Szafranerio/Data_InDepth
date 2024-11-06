import random
class Hat:
    houses = ['Gdynia', 'Sopot', 'Gdańsk', 'Warszawa']
    @classmethod
    def sort(cls, name):
        print(name, 'is in', random.choice(cls.houses))
Hat.sort('Harry')
