class Car():

    def __init__(self, make, model, year) -> None:

        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """Return a neatly formatted name."""
        long_name = f"{str(self.year)}, {self.make}, {self.model}"
        print(long_name)
    
    def set_odometer(self):
        """Setting a new value for odometer."""
        print(f"This car has {str(self.odometer_reading)} miles on it.")

    def update_odometer(self, mileage):
        """Sets the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer.")
    
    def increment_odometer(self, miles):
        """Set the odometer according to how many miles the car traveled."""
        self.odometer_reading += miles


class Battery():

    def __init__(self, battery_size=70) -> None:
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {str(self.battery_size)} -kWh battery.")
    
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        message = f"This car can go approximately {str(range)}"
        message += " miles on a full charge."
        print(message)
    
    def upgrade_battery(self):
        """Set capacity"""
        if self.battery_size <= 84:
            self.battery_size = 85


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year) -> None:
        """Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car."""
        super().__init__(make, model, year)
        self.battery = Battery()

my_car = Car("Audi", "a5", 2016)
my_car.get_descriptive_name()
# my_car.update_odometer(50)
# my_car.increment_odometer(250)
# my_car.set_odometer()
# my_electric = ElectricCar("Tesla", "s", 2018)
# print(my_electric.get_descriptive_name())
# my_electric.update_odometer(100)
# my_electric.set_odometer()
# my_electric.update_odometer(50)

# my_car = ElectricCar("Tesla", "Model S", "2018")
# print(my_car.get_descriptive_name())
# my_car.battery.describe_battery()
# my_car.battery.get_range()

new_car = ElectricCar("Nissan", "LEAF", "2018")
new_car.get_descriptive_name()
new_car.battery.describe_battery()
new_car.battery.get_range()
new_car.battery.upgrade_battery()
new_car.battery.get_range()