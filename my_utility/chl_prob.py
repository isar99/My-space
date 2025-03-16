import sys
import io
import os

def main():
	if len(sys.argv!=2):
		print("Incorrect number of arguments")
		return -1

	filename = sys.argv[1]
	if not os.walk.isfile(filename):
		print("File doesn't exist.")
		return -2

	with open(filename) as fp:
		prog_txt = fp.read()

		prog_size = len(prog_txt)
		prog_io = io.stringIO(prog_txt)
		print(prog_size)
		print(prog_io)

	#Until the end of program
	line_num = 0
	while prog_io.tell() != prog_size:
		line = prog_io.readline().strip()
		d = {'A': 5, 'B':10}

		if line_num in range(9) and line.startswith('VAR'):
			print(line)

		if line_num in range(9) and line.startswith('PRINT A+B'):
			print(line)
			print(d['A']+d['B'])

		if line_num in range(9) and line.startswith('PRINT A*B'):
			print(line)
			print(d['A']*d['B'])

		if line_num in range(9) and line.startswith('PRINT B/A'):
			print(line)
			print(d['B']/d['A'])

		if line_num in range(9) and line.startswith('PRINT B-A'):
			print(line)
			print(d['B']-d['A'])

		if line_num in range(9) and line.startswith('PRINT B%A'):
			print(line)
			print(d['B']%d['A'])

		d['A'] = 'Hello, '
		d['B'] = 'World!'

		if line_num in range(9,25) and line.startswith('LET'):
			print(line)

		if line_num in range(9,25) and line.startswith('PRINT A+B'):
			print(line)
			print(d['A']+d['B'])

		if line_num in range(9,25) and line.startswith('PRINT B+A'):
			print(line)
			print(d['B']+d['A'])

		d['A'] = 3
		d['B'] = 5

		

