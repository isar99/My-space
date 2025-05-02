arr = []
def append():
	n = int(input('append '))
	return arr.append(n)

def insert():
	m,o= input('insert  ').split()
	return arr.insert(int(m),int(o))

def remove():
	r = int(input('remove '))
	return arr.remove(r)


def pop():
	return arr.pop()

def sort():
	return arr.sort()

def reverse():
	return arr.reverse()
#print(re)

def pri():
	print(arr)

functions = {'append': append, 'insert': insert, 'remove': remove, 'pop': pop, 'sort': sort, 'reverse': reverse, 'print': pri}

N = int(input("Enter the number of command: "))
#print("Commands:")
for n in range(N):
	function_name = input("Enter the function name: ")
	functions[function_name]()
	