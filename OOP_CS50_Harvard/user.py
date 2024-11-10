class User():
    def __init__(self, first_name, second_name, age, country, sex):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        self.country = country
        self.sex = sex
        self.login = 0

    def login_attempts(self):
        print(f'Current user have made {self.login} login attempts')

    def increment_user_attempts(self, number):
        self.login += number

    def reset(self):
        self.login = 0

    def greet_user(self):
        print(f'Hello {self.first_name} {self.second_name}, you are {self.age} years old,your sex is {self.sex} and you come from {self.country}. User made {self.login}')

class Priveliges():
    def __init__(self, priveliges = ('Can add posts', 'Can remove posts', 'Can add or delete users')):
        self.priveliges = priveliges
    def show_rights(self):
        print('Admin have several rights such as')
        print(self.priveliges)
        
class Admin(User):
    def __init__(self, first_name, second_name, age, country, sex):
        super().__init__(first_name, second_name, age, country, sex)
        self.privilage = Priveliges()

    def show_rights(self):
        print('Admin have several rights such as')
        print(self.rights)
        
    def greet_admin(self):
        print(f'Hello {self.first_name} {self.second_name}, you are {self.age} years old,your sex is {self.sex} and you come from {self.country}. You are an admin!')

user1 = User('Bartek', 'Szafran', 27, 'Poland', 'Male')
user2 = User('Tom', 'Brown', 21, 'England', 'Male')
admin = Admin('Mark', 'Godt', 45, 'Denmark', 'Male')


user1.greet_user()
user2.greet_user()
user1.increment_user_attempts(12)
user1.login_attempts()
user1.reset()
user1.login_attempts()
user2.increment_user_attempts(100)
user2.login_attempts()
user2.reset()
user2.login_attempts()
admin.greet_admin()
admin.privilage.show_rights()
