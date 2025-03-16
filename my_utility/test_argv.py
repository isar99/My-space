#!/usr/bin/env python3
import sys

print(sys.argv)

for arg in enumerate(sys.argv):
    print(f'{arg[0]}: {arg[1]}')
