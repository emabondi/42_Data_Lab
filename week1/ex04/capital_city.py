import sys

states = {
"Oregon" : "OR",
"Alabama" : "AL",
"New Jersey": "NJ",
"Colorado" : "CO"
}
capital_cities = {
"OR": "Salem",
"AL": "Montgomery",
"NJ": "Trenton",
"CO": "Denver"
}
if __name__=="__main__":
	if len(sys.argv) != 2:
		exit(0)
	if states.get(sys.argv[1]) == None:
		print("Unknown state")
		exit(0)
	print (capital_cities.get(states.get(sys.argv[1])))