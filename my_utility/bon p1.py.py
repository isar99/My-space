integer = int(input("Integer: "))
x =0
for x in range(integer):
	if x**2 == integer or x**3 == integer:
		print(True)
		break
	else:
		if x < (integer-1) :
			continue
		else:
			print(False)