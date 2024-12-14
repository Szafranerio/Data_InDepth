import random

def random_num(low, high, n):
    for _ in range(n):
        yield random.randint(low, high)
        
for num in random_num(1,3,6):
    print(num)