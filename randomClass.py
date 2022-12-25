class Chair():
	
    def __init__(self, style, creator, price):

        self.style = style
        self.creator = creator
        self.price = price 

    def describe_chair(self):
        """Simulate a price description of a chair."""
        chair = "This chair is from {} style and its creator's name is {} and it costs {:.2f} bucks.".format(self.style, self.creator, self.price)

        return chair

chair = Chair("Late roman", "Kye", 100)
print(chair.describe_chair())
    