import random

save = []

class Die():
    def __init__(self):
        self.sides = 6

    def roll_die(self, rolls = 20):
        die = [1, 2, 3, 4, 5, 6]
        for n in range(1, rolls + 1):
            a = random.choice(die)
            print(f'{n} throw of die and its value is {a}')
            save.append(a)

my_roll = Die()
my_roll.roll_die()
print(save)