#!/usr/bin/env python3

import sys

NUMS = [1, 2, 3, 1]

def findCount(N):
		if N == 0:
				return 1

		# Memoization
		table = [0 for _ in range(N+1) for _ in range(len(NUMS))]
		
		# base cases
		table[1] = 2
		table[2] = 5
		table[3] = 13

		for i in range(4, N+1):
				table[i] = 2*table[i-1] + table[i-2] + table[i-3]
		
		return table[N]

if __name__ == '__main__':
		for line in sys.stdin:
				line = line.rstrip()
				print(findCount(int(line)))
