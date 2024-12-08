try:
    #Want to try code, it may have an error
    result = 10 + 10
except:
    print('Something is wrong')
else:
    print('The result is')
    print(result)
   
try:
    f = open('testfile', 'w')
    f.write('Write test line')
except TypeError:
    print('There was type error')
except OSError:
    print('There is OS error')
finally:
    print('Always running')

def ask_for_int():
    while True:
        try:
            result = int(input('PLease provide the number: '))
        except:
            print('Its not the number')
            continue
        else:
            print('Thanks your number is accepted')
            break
        finally:
            print('End')
     
ask_for_int()

#1

for i in ['a','b','c']:
    
    try:
        print(i**2)
    except:
        print('There is smth wrong!')
        
#2 

x = 5
y = 0

try:
    z = x/y
    print(z)
except:
    print('You cannot divide by zero')
finally:
    print('Check your data again')
    
#3

def ask():
    while True:
        try:
            x = int(input('Please enter the number to be squred: '))
        except:
            print('It is not the number!')
            continue
        else:
            print(f'The square of number is {x**2}')
            break
        finally:
            print('Hello its worst program ever')

ask()