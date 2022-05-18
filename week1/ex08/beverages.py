class HotBeverage:
	def __init__(self):
		self.price = 0.30
		self.name = "hot beverage"

	def description(self):
		d = "Just some hot water in a cup"
		return (d)

	def __str__(self):
		print(f"name : {self.name}")
		print(f"price : {self.price}")
		print(f"description : {self.description()}")
		#return ("")

if __name__=="__main__":
	a = HotBeverage()
	print(a)