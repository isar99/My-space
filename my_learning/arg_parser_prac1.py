import argparse
import math

parser = argparse.ArgumentParser(description="Calculate volume of cylinder")
parser.add_argument('--radius', '-r', type=int, metavar='', required=True, help='Radius of the cylinder')
parser.add_argument('--height', '-ht', type=int, metavar='', required=True, help='Height of the cylinder')
group = parser.add_mutually_exclusive_group()
group.add_argument('--quiet', '-q', action='store_true', help='Print quiet')
group.add_argument('--verbose', '-v', action='store_true', help='Print verbose')

args = parser.parse_args()

def cylinder_volume(radius, height):
	volume = math.pi*(radius**2)*(height)
	return volume

if __name__ =='__main__':
	vol = cylinder_volume(args.radius, args.height)

	if args.quiet:
		print(vol)
	elif args.verbose:
		print(f'Volume of cylinder with radius {args.radius} and height {args.height} is {vol}')
	else:
		print(f'Volume is {vol}')
