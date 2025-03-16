import time
from math import pi

def calculate_time(func):

	def inner(*args,**kwargs):

		start = time.time()
		
		func(*args,**kwargs)
		
		end = time.time()
		tot_time = end - start

		print(f"The calculated time for {func.__name__} is {tot_time}. ")

	return inner

@calculate_time
def circle_area(radius):

	time.sleep(2)
	print(pi*radius*radius)
