def create_cubes(n):
    for x in range(n):
        yield x**3
        
list(create_cubes(9))

#Fibonaci

def gen_fibon(n):
    a = 1
    b = 1
    
    for i in range(n):
        yield a
        a,b = b,a+b
for n in gen_fibon(10):
    print(n)
    
    
def simple_gen():
    for x in range(3):
        yield x
for x in simple_gen():
    print(x)
    
g = simple_gen()
print(next(g))
print(next(g))
print(next(g))


#Squares generator

def generate_squares(n):
    for x in range(n):
        yield x**2
        
list(generate_squares(5))

#Random numbers between low and high
import random

def random_num(low, high, n):
    for _ in range(n):
        yield random.randint(low, high)
        
for num in random_num(1,10,6):
    print(num)
        
        
