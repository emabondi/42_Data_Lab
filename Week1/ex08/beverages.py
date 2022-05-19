class HotBeverage:
	def __init__(self):
		self.price = 0.30
		self.name = "hot beverage"

	def description(self):
		d = "Just some hot water in a cup"
		return (d)

	def __str__(self):
		return (f"name : {self.name}\nprice : {self.price}\ndescription : {self.description()}")


	class Coffee:
		def __init__(self):
			self.price = 0.40
			self.name = "coffee"

		def description(self):
			d = "A coffee, to stay awake."
			return (d)
		
		def __str__(self):
			return (f"name : {self.name}\nprice : {self.price}\ndescription : {self.description()}")
	
	class Tea:
		def __init__(self):
			self.price = 0.30
			self.name = "tea"

		def description(self):
			d = "Just some hot water in a cup."
			return (d)
		
		def __str__(self):
			return (f"name : {self.name}\nprice : {self.price}\ndescription : {self.description()}")


	class Chocolate:
		def __init__(self):
			self.price = 0.50
			self.name = "chocolate"

		def description(self):
			d = "Chocolate, sweet chocolate..."
			return (d)
		
		def __str__(self):
			return (f"name : {self.name}\nprice : {self.price}\ndescription : {self.description()}")


	class Cappuccino:
		def __init__(self):
			self.price = 0.45
			self.name = "cappuccino"

		def description(self):
			d = "Un po' di Italia nella sua tazza!"
			return (d)
		
		def __str__(self):
			return (f"name : {self.name}\nprice : {self.price}\ndescription : {self.description()}")


	
if __name__=="__main__":
	a = HotBeverage()
	b = HotBeverage.Coffee()
	c = HotBeverage.Tea()
	d = HotBeverage.Chocolate()
	e = HotBeverage.Cappuccino()
	print(f"{a}\n{b}\n{c}\n{d}\n{e}")
	print(b)
	print(c)
	print(d)
	print(e)