class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.range = 0

    def get_descriptive(self):
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()

    def read_range(self):
        print(f'The range of car is {self.range} km')

    def update_range(self, new_range):
        self.range = new_range

    def increment_range(self, km):
        self.range += km
        print(f'The newest range is {self.range}')


class Battery():
    def __init__(self, battery_size = 75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f'This cas has batter with capacity of {self.battery_size} kWh.')

    def battery_range(self):
        if self.battery_size <= 75:
            range = 260
        elif self.battery_size == 100:
            range = 300
            
        print(f'The range for this car is max {range}')

    def upgrade_battery(self, new_size=100):
        self.battery_size = new_size
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        print(f'This car has battery size of {self.battery_size}')


my_car = Car('audi', 'a4', 2022)
print(my_car.get_descriptive())
my_car.update_range(27)
my_car.read_range()
my_car.increment_range(1000)

my_tesla = ElectricCar('tesla', 's', 2019)
print(my_tesla.get_descriptive())
my_tesla.battery.describe_battery()
my_tesla.battery.battery_range()

my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.battery_range()
