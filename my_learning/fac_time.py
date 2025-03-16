import time
import math

def calculate_time(func):

	def inner(*args,**kwargs):

		start = time.time()
		
		func(*args,**kwargs)
		
		end = time.time()
		tot_time = end - start

		print(f"The calculated time for {func.__name__} is {tot_time}. ")

	return inner

@calculate_time
def factorial(n):

	time.sleep(2)
	print(math.factorial(n))

