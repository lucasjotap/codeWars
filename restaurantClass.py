class Restaurant():
    """Model of a restaurant"""
    def __init__(self, name, cuisine):
        """Initialize restaurant"""
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe(self):
        """Describes restaurant's name and cuisine"""
        vowels = "aeiou"
        if self.cuisine[0].lower() in vowels:
            print(f"{self.name.title()} is an {self.cuisine.title()} restaurant.")
        else:
            print(f"{self.name.title()} is a {self.cuisine.title()} restaurant.")

    def open_restaurant(self):
        """Display open sign."""
        print(self.name.title() + " is now open")

    def set_number_served(self, new_served):
        """Set the number of customers that have been served."""
        self.number_served += new_served
        i = "Number of served customers: " + str(self.number_served)
        return i

    def increment_number_served(self, increment):
        """Increments served numbers of customers"""
        self.number_served += increment     

class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine):
        """Creating a child class for an icecream stand."""
        super().__init__(name, cuisine)

        self.flavors = ["chocolate", "vanilla", "strawberry"]

    def flavors_available(self):
        """Display flavors."""
        print("\nFlavors availble: ")
        for flavor in self.flavors:
            print(f"\tThe {flavor} flavor is available.")

french = Restaurant("Lasgna House", "Italian")
ice_cream_stand = IceCreamStand("Charlies", "French")
french.describe()
ice_cream_stand.describe()
ice_cream_stand.flavors_available()
