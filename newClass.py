class Car():

    def __init__(self, make, model, year) -> None:

        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """Return a neatly formatted name."""
        long_name = f"{str(self.year)}, {self.make}, {self.model}"
        return long_name
    
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

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year) -> None:
        """Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car."""
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {str(self.battery_size)} -kWh battery.")


# my_car = Car("Audi", "a5", 2016)
# print(my_car.get_descriptive_name())
# my_car.update_odometer(50)
# my_car.increment_odometer(250)
# my_car.set_odometer()
# my_electric = ElectricCar("Tesla", "s", 2018)
# print(my_electric.get_descriptive_name())
# my_electric.update_odometer(100)
# my_electric.set_odometer()
# my_electric.update_odometer(50)

my_car = ElectricCar("Tesla", "Model S", "2018")
print(my_car.get_descriptive_name())
my_car.describe_battery()

