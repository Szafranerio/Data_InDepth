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

amici = Restaurant('Amici', 'Italian', 'from 16-20')
fusion = Restaurant('Fusion', 'Danish', 'from 14-22')
kro = Restaurant('Kro', 'French', 'from 15-23')
amici.set_number_served(12)
fusion.set_number_served(14)
kro.set_number_served(123)

amici.describe_restaurant()
fusion.describe_restaurant()
kro.describe_restaurant()