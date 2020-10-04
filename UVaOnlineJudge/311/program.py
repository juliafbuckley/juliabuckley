#!/usr/bin/env python3

# Julia Buckley
# Challenge 09

import sys

# Functions

def calcBlocks(one, two, three, four):
		# Greedy Algorithm structure: fours up top, then threes, etc
		bricks = []
		rows = 0

		for f in range(four):
				bricks.append(4)
		for th in range(three):
				bricks.append(3)
		for tw in range(two):
				bricks.append(2)
		for o in range(one):
				bricks.append(1)

		while bricks:
				b = bricks.pop(0)
				if b == 4:
						rows += 1
				else:
						match = False
						index = 0
						curRow = b
						
						pop = []
						while curRow < 4:
								try:			
										if bricks[index] + curRow <= 4:
												curRow += bricks[index]
												pop.append(index)
												index += 1
										else:
												index += 1

										if curRow == 4:
												rows += 1
												if len(pop) == len(bricks):
														bricks.clear()
														break
												else:
														for p in pop:
																bricks.pop(p)
								except:
										rows += 1
										if bricks:
												bricks = bricks.clear()
										break

		print(rows)

def main():
		for line in sys.stdin:
				blocks = list(map(int, line.split()))
				calcBlocks(blocks[0], blocks[1], blocks[2], blocks[3])


# Main execution
if __name__ == '__main__':
		main()
