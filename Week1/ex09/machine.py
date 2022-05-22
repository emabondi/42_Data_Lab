import random
from beverages import *

class CoffeeMachine:
	def __init__(self):
		self.served = 0

	class EmptyCup(HotBeverage):
		def __init__(self, name = "empty cup", price = 0.90, description = "An empty cup?! Gimme my money back!"):
			super().__init__(name, price, description)

	class BrokenMachineException(Exception):
		def __init__(self, *args: object) -> None:
			super().__init__("This coffee machine has to be repaired.")

	def repair(self):
		self.served = 0
		print ("The coffe machine has been repaired")

	def serve(self, drink):
		if self.served == 10:
			raise self.BrokenMachineException()
		self.served += 1
		if random.randint(1, 2) % 2 == 0:
			return drink()
		else:
			return self.EmptyCup()

if __name__=="__main__":
	a = [HotBeverage, Coffee, Tea, Chocolate, Cappuccino] * 3
	c = CoffeeMachine()
	for e in a:
		try:
			z = c.serve(e)
			print (z)
		except c.BrokenMachineException as ex:
			print(ex)
			c.repair()
