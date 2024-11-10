class Restaurant():
    def __init__(self, restaurant_name, cusine_type, open):
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type
        self.open = open
        self.numbered_served = 0

    def describe_restaurant(self):
        print(f'{self.restaurant_name.title()}, this is {self.cusine_type.title()} restaurant and is open daily {self.open}, cusotmer served {self.numbered_served}')

    def set_number_served(self, number):
        self.numbered_served += number


class IceCreams(Restaurant):
    def __init__(self, restaurant_name, cusine_type, open):
        super().__init__(restaurant_name, cusine_type, open)
        self.flavors = ['Strawberry', 'Chocolate', 'Lemon']

    def show_flavors(self):
        print('Iceee have several flavors such as:')
        print(self.flavors)


amici = Restaurant('Amici', 'Italian', 'from 16-20')
fusion = Restaurant('Fusion', 'Danish', 'from 14-22')
kro = Restaurant('Kro', 'French', 'from 15-23')
amici.set_number_served(12)
fusion.set_number_served(14)
kro.set_number_served(123)

amici.describe_restaurant()
fusion.describe_restaurant()
kro.describe_restaurant()

my_ice_creams = IceCreams('Iceee', 'Deserts', 'from 10-18')
my_ice_creams.set_number_served(10)
my_ice_creams.describe_restaurant()
my_ice_creams.show_flavors()
