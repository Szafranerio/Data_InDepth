class Restaurant():
    def __init__(self, restaurant_name, cusine_type, open):
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type
        self.open = open
    
    def describe_restaurant(self):
        print(f'{self.restaurant_name.title()}, this is {self.cusine_type.title()} restaurant and is open daily {self.open}')


amici = Restaurant('Amici', 'Italian', 'from 16-20')
fusion = Restaurant('Fusion', 'Danish', 'from 14-22')
kro = Restaurant('Kro', 'French', 'from 15-23')


amici.describe_restaurant()
fusion.describe_restaurant()
kro.describe_restaurant()