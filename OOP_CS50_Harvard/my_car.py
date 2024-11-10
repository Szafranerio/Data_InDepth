from car import *

my_car = Car('Audi', 'Q9', 2021)
print(my_car.get_descriptive())
my_car.update_range(50)
my_car.read_range()

my_electric_car = ElectricCar('Polestar', 'Sport', 2019)
print(my_electric_car.get_descriptive())
my_electric_car.battery.describe_battery()
my_electric_car.battery.battery_range()