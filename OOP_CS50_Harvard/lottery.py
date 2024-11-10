import random

NUMBERS = range(1, 4)
WINNMBERS = range(1, 5)

user_numbers = []
user_super_number = []

win_numbers = []
winsup_numbers = []


class Lotery():
    def __init__(self):
        pass

    def user_numbers(self, rolls=4, rolls_super_number=1):
        for i in range(1, rolls + 1):
            normal_numbers = int(input('Pick a number from the range 1-60: '))
            user_numbers.append(normal_numbers)
        for x in range(1, rolls_super_number + 1):
            super_number = int(
                input('Pick the super number from the range 1-5: '))
            user_super_number.append(super_number)


class WinNumbers():
    def __init__(self):
        pass

    def lottery_win(self, rolls=4, rolls_super_numbers=1):
        for n in range(1, rolls + 1):
            wn = random.choice(NUMBERS)
            win_numbers.append(wn)
        for x in range(1, rolls_super_numbers + 1):
            wsn = random.choice(WINNMBERS)
            winsup_numbers.append(wsn)
            print(f'Winning numbers: {win_numbers}')
            print(f'Super numbers: {wsn}')


class Check():
    def __init__(self, user_numbers, win_numbers):
        self.user_numbers = user_numbers
        self.win_numbers = win_numbers

    def check_winner(self):
        if win_numbers == user_numbers:
            print('Winner')
        else:
            print('You lost')

    def my_ticker(self, user_numbers, win_numbers, count=0):
        while user_numbers != win_numbers:
            drawn_numbers = [random.choice(NUMBERS)
                             for _ in range(len(user_numbers))]
            count += 1
            print(f'{count}: Drawn numbers: {drawn_numbers}')

            if drawn_numbers == win_numbers:
                print("You have matched the winning numbers!")
                break


user = Lotery()
user.user_numbers()
print(user_numbers)
print(user_super_number)

win = WinNumbers()
win.lottery_win()
print(win_numbers)
print(winsup_numbers)

check = Check(user_numbers, win_numbers)
check.check_winner()
check.my_ticker(user_numbers, win_numbers)
