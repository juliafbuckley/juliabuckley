#!/usr/bin/env python3

# Julia Buckley
# Challenge 07

import sys

# Globals
HOPS_DICT = {
				0: (4, 6),
				1: (6, 8),
				2: (7, 9),
				3: (4, 8),
				4: (0, 3, 9),
				5: (),
				6: (0, 1, 7),
				7: (2, 6),
				8: (1, 3),
				9: (2, 4)
				}

# Functions

def calcN(start, hops, nums):
		# Read the most rtecent digit in the nums array, and make recursive calls
		# based on the values in the dict
		
		hops = int(hops)
		start = int(start)

		if len(nums) == 0:
				nums = [start]
		
		if len(nums) == hops:
				print("".join(map(str, nums)))
				return
		
		for d in HOPS_DICT[start]:
				yield from calcN(d, hops, nums + [d])


def main():
		count = 0
		for line, numbers in enumerate(map(str.split, sys.stdin)):
				nums = []
				
				if len(numbers) <= 1:
						break

				if line:
						print()
				
				list(calcN(numbers[0], numbers[1], nums))

# Main Execution

if __name__ == '__main__':
		main()
