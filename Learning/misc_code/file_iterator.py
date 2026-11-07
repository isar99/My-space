f = open('turtle_stuff.py')
f.readline()
import sys
f.readline()
print(sys.path)
for line in open('turtle_stuff.py'):
	print(line.upper())