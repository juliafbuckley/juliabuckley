#!/usr/bin/env python3

import sys
import pprint

# Functions

def rotate_matrix(N, m):
# Transpose the matrix
		for i in range(N):
				for j in range(i, N):
						temp = m[i][j]
						m[i][j] = m[j][i]
						m[j][i] = temp

# Flip the matrix horizontally
		for i in range(N):
				for j in range(N//2):
						temp2 = m[i][j]
						m[i][j] = m[i][N-1-j]
						m[i][N-1-j] = temp2

# Print to stdout
		for i in range(N):
				for j in range(N):
						if j != N-1:
								print(m[i][j], end=" ")
						elif j == N-1:
								print(m[i][j], end="")
				if i != N-1:
						print("")
				elif i == N-1:
						pass

def define_matrices(array, index):
		N = array[index]
		if N == 0:
				sys.exit()
		mat = [[0]*N]*N
		temp = []
		index = index+1
		
		for j in range(N):
				for i in range(N):
						temp.append(array[index+i])
				index = index+N
				mat[j] = temp
				temp = []

		rotate_matrix(N, mat)
		if (index+1) != len(array):
				print("\n")
		else:
				print("")
		define_matrices(array, index)


# Main execution

if __name__ == '__main__':
		m = []
		for line in sys.stdin:
				line = line.rstrip()
				for n in line.split():
						m.append(int(n))
		define_matrices(m, 0)
