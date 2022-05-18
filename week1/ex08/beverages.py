class HotBeverage:
	def __init__(self):
		self.price = 0.30
		self.name = "hot beverage"

	def description(self):
		d = "Just some hot water in a cup"
		return (d)

	def __str__(self):
		return (f"name : {self.name}\nprice : {self.price}\ndescription : {self.description()}")

if __name__=="__main__":
	a = HotBeverage()
	print(a)