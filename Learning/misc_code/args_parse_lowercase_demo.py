import argparse
def lowercase_args(val):
	updated_val = val.lower()
	print(updated_val)

parser = argparse.ArgumentParser(prog = 'PROG')
parser.add_argument('foo', type = lowercase_args)
parser.parse_args(['MoNdAy'])