a = [42, "42", "quarante-deux", 42.0, True, [42], {42 : 42}, (42, ), set()]

for val in a:
	print("{} has a type {}".format(val, type(val)))