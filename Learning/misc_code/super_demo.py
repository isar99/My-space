# Example 1

# class Emp():
# 	def __init__(self, id, name, Add):
# 		self.id = id
# 		self.name = name
# 		self.Add = Add


# class Freelance(Emp):
# 	def __init__(self, id, name, Add, Emails):
# 		super().__init__(id, name, Add)
# 		self.Emails = Emails

# Emp1 = Freelance(2, "Isar", "Noida", "Ish@hmail.com")
# print(f'Id is -> {Emp1.id}')
# print(f'Name is -> {Emp1.name}')
# print(f'Address is -> {Emp1.Add}')
# print(f'Email is -> {Emp1.Emails}')



# Example 2

class Emp():
	def __init__(self, id, name, Add):
		self.id = id
		self.name = name
		self.Add = Add

	def Display(self):
		print(self.id, self.name)


class Freelance(Emp):
	def __init__(self, id, name, Add, Emails):
		super().__init__(id, name, Add,)
		super().Display()
		self.Emails = Emails

Emp1 = Freelance(2, "Isar", "Noida", "Ish@hmail.com",)
print(f'Id is -> {Emp1.id}')
print(f'Name is -> {Emp1.name}')
print(f'Address is -> {Emp1.Add}')
print(f'Email is -> {Emp1.Emails}')
# print(f'Display -> {Emp1.Display()}')