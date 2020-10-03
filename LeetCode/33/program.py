#!/usr/bin/env python3

# Julia Buckley
# Challenge04: Binary Search O(logn)
# Plan: Find pivot point, then binary search from there using pivot

import bisect
import sys

def binary_search_pivot(array, pivot, target):
		low = pivot		# start of original array (min)
		length = len(array)
		high = pivot - 1 	# end of original array (max)
		start = 0
		end = length-1

		
		# find which side of array to bisect using pivot
		# if the target is greater than the last value of the rotated array
		if target > array[end]:
				end = high
				shift = 0
		elif target < array[end]:
				start = low
				shift = start
		else: 
				targetInd = end
				print("{} found at index {}".format(target, targetInd))
				return 0
		
		subarray = array[start:(end+1)]
		# conduct binary search on new subarray
		index = bisect.bisect_left(subarray, target)
		if index < len(subarray) and subarray[index] == target:
				targetInd = index

		try:
				print("{} found at index {}".format(target, targetInd+shift))
		except:
				print("{} was not found".format(target))


def find_pivot(array, target):
		# Objective: find the index of the smallest int in the array
		# define initial low and high indexes
		low = 0
		high = len(array) - 1	
		
		#first check if it's in order
		if array[low] < array[high]:
				binary_search_pivot(array, 0, int(target))
				return 0

		while (low <= high):
				# redefine mid
				mid = (low+high)//2
				
				# check if (mid + 1) is pivot
				if mid < high and array[mid+1] < array[mid]:
						binary_search_pivot(array, mid+1, int(target))
						break
				
				# check if mid is pivot
				elif mid > low and array[mid] < array[mid-1]:
						binary_search_pivot(array, mid, int(target))
						break
				
				# pivot not found, split in half
				if array[high] > array[mid]:
						high = mid - 1
				else:
						low = mid + 1

			
def split_input(inpt):
		index = 0
		a = []
		for line in inpt:
				if not index % 2:				# if it is a rotated array
						for n in line.split():
								a.append(int(n))
						find_pivot(a, inpt[index+1])
						a.clear()
				else:
						pass
				index = index + 1


# Main

if __name__ == '__main__':
		inpt = []
		for line in sys.stdin:
				line = line.rstrip()
				inpt.append(line)
		split_input(inpt)

