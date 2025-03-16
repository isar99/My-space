def fibonacci(num):
	sum =0
	for el in range(num):
		sum = sum+el
		yield sum

for number in fibonacci(5):
	print(number)
