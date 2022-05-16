import sys

if (len(sys.argv) != 4 or not sys.argv[1].isdigit() or not sys.argv[2].isdigit() or not sys.argv[3].isdigit()):
	print("Error")
	exit(0)
x = (int)(sys.argv[1]) * 3600
y = (int)(sys.argv[2]) * 60
z = (int)(sys.argv[3])
print(x + y + z)