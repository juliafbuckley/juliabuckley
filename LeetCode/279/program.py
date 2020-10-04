#!/usr/bin/env python3

import sys
import math

# Functions

def perfSquares(n):
		
		s = int(math.sqrt(n))
		
		# initialize
		table = [0] * (n+1)

		# base case - if perfect square
		if s*s == n:
				table[n] = 1

		for i in range(1, n+1):
				if not table[i]:
						table[i] = 1 + min(table[i - num*num] for num in range(1, s+1) if (i - num*num) >= 0)
		
		return table[n]


def main():
		for line in sys.stdin:
				line = line.rstrip()
				print(perfSquares(int(line)))

# Main
if __name__ == '__main__':
		main()
