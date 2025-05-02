# We are just going to learn about different types of method
# There are 3 types of method :- 
# 	1)Instance Method, 
# 	2)Class Method, 
# 	3)Static Method
# Class Method and Static Method are bound to class only and not to the object of the class.
# In Class Method, @classmethod decorator is used.
# In Static Method, @staticmethod decorator is used.
# In Instance Method, 'self' is passed as an argument in function.
# In Class Method, 'cls' is passed as an argument in function.
# In Static Method, no argument is passed as an argument in function.
# Class method can acess and modify the class state whereas Static method cannot be accessed and modified.
# In general, static method know nothing about the class state, on the other hand class method must have class as a parameter.
# We generally use class method for factory methods.
# We generally use static method to create utility functions.
# Instance method have 2 types :-
# 	1) Accessor Method - get the value
# 	2) Static Method - set the value

class Student:
	school = 'DPS'

	def __init__(self, m1, m2, m3):
		self.m1 = m1
		self.m2 = m2
		self.m3 = m3

	def avg(self):
		return (self.m1 +self.m2 + self.m3)/3

	@classmethod
	def cls_method(cls):
		return cls.__name__

	@staticmethod
	def static_method(name):
		fn = mn = ln = ''
		splits = name.split()
		fn = splits[0]
		if len(splits) > 1:
			ln = splits[-1]
		if len(splits) > 2:
			mn = " ".join(splits[1:-2])
		return fn, mn, ln

if __name__== '__main__':
	s1 = Student(93, 87, 78)
	print(s1.avg())
