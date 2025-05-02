import math
import argparse
def perfect_square(string):
	val = int(string)
	sqrt = math.sqrt(val)
	if sqrt != int(sqrt):
		msg = f'{string} is not a perfect square'
		raise argparse.ArgumentTypeError(msg)
	result = f'{sqrt} is the square root of {val}'
	print(result)

parser = argparse.ArgumentParser(prog = 'PROG')
parser.add_argument('foo', type = perfect_square)
parser.parse_args(['7'])

