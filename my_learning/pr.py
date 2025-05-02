array = [2,0,2,0,4]
sum = 0

for i,elment in enumerate(array[:(len(array)-1):1]):
	x = min(array[i], array[i+1])
	sum = sum+x
print(f"Desired output is {sum}")