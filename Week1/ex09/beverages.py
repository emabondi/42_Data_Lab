class HotBeverage:
	def __init__(self, name = "hot beverage", price = 0.30, description = "Just some hot water in a cup"):
		self.name = name
		self.price = price
		self.desc = description

	def description(self):
		return self.desc

	def __str__(self):
			return "name : {}\nprice : {:.2f}\ndescription : {}\n".format(self.name, self.price, self.description())

class Coffee(HotBeverage):
		def __init__(self, name = "coffee", price = 0.40, description = "A coffee, to stay awake."):
			super().__init__(name, price, description)
	
class Tea(HotBeverage):
		def __init__(self, name = "tea", price = 0.30, description = "Just some hot water in a cup."):
			super().__init__(name, price, description)
		
class Chocolate(HotBeverage):
		def __init__(self, name = "chocolate", price = 0.50, description = "Chocolate, sweet chocolate..."):
			super().__init__(name, price, description)
		
class Cappuccino(HotBeverage):
		def __init__(self, name = "cappuccino", price = 0.40, description = "Un po' di Italia nella sua tazza!"):
			super().__init__(name, price, description)
			
if __name__=="__main__":
	a = HotBeverage()
	b = Coffee()
	c = Tea()
	d = Chocolate()
	e = Cappuccino()
	print(f"{a}{b}{c}{d}{e}")