def pretty_print(matrix):
	for row in matrix:
		print(row)
	print()

def fold(matrix):
	matrix_size = len(matrix)	
	for y1 in range(0, matrix_size - 1):
		for x1 in range(matrix_size - 1, 0, -1):
			if (x1 < y1):
				continue
			num = matrix[y1][x1]
			matrix[y1][x1] = matrix[x1][y1]
			matrix[x1][y1] = num
	return matrix

def calc(matrix):
	print("ORIGINAL")
	pretty_print(matrix)

	folded_matrix = fold(matrix)

	print("FOLDED")
	pretty_print(folded_matrix)


print("2X2 MATRIX")
matrix = ([1, 2], 
		  [4, 3])
calc(matrix)

print("3X3 MATRIX")
matrix = ([7, 5, 9],
		  [3, 4, 12],
		  [4, 6, 11])
calc(matrix)

print("4X4 MATRIX")
matrix = ([1, 5, 6, 8], 
		  [10, 12, 14, 56], 
		  [4, 2, 1, 0], 
		  [10, 19, 42, 7])
calc(matrix)

print("5X5 MATRIX")
matrix = ([1, 5, 6, 8, 0], 
		  [10, 12, 14, 56, 7], 
		  [4, 2, 1, 0, 43], 
		  [10, 19, 42, 7, 3],
		  [3, 66, 32, 12, 9])
calc(matrix)

