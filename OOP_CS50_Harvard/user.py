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
        print(f'Hello {self.first_name} {self.secon