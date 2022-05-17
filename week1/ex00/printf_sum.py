import sys
if __name__=="__main__":

	if (len(sys.argv) != 3 or not(sys.argv[1].isnumeric()) or not(sys.argv[2].isnumeric())):
		print("Error")
		exit(0)
	x = (int)(sys.argv[1])
	y = (int)(sys.argv[2])
	print(x + y)