S1 = input("Please enter sentence: ")
S2 = input("Please enter string: ")
C = input("Only enter Y or N: ")
l = int(input("An integer: "))
if S1.find(S2):
	if S2.index(S1[0])==l:
		if C == 'Y':
	 		if S2 in S1.split(""):
	 			print(f"Hack -> {l}")
	 	# C == 'N':
	 	# 	print(f"Hack -> {l}")
elif not S1.find(S2.split()):
 	print('Goodbye Watson')