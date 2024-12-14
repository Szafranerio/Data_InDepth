#Counts the list 

from collections import Counter
my_list = [1,2,3,4,4,1,2,3,4,1,424,21,3,123,12,12,31,24,125,261,6,14,5,324,12]
Counter(my_list)

letters = 'aaaaabbbbbvvvvvvddddeeeeff'
c = Counter(letters)

#Return most common 
c.most_common(2)

#List single letters
list(c)


from collections import defaultdict
#Assigne values for dictionary but when unsure you can use defauklt dict to run program
d = {'a':10}
d = defaultdict(lambda:0)
d['correct'] = 100
d['correct']
d['wrong key']

my_tuple = (10,20,30)
my_tuple[0]

from collections import namedtuple
Dog = namedtuple('Dog',['age', 'breed', 'name'])
sammy = Dog(age=5, breed='Husky', name='Sammy')
sammy.age
sammy.breed