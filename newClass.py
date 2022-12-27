class Car():

    def __init__(self, make, model, year) -> None:

        self.make = make
        self.model = model
        self.year = year
    
    def get_descriptive_name(self):
        """Return a neatly formatted name."""
        long_name = f"{str(self.year)}, {self.make}, {self.model}"
        return long_name

my_car = Car("Audi", "a5", 2016)
print(my_car.get_descriptive_name())