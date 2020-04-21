'''
A Toeplitz matrix is a matrix where every left-to-right-descending diagonal has the same element. Given a non-empty matrix arr, write a function that returns true if and only if it is a Toeplitz matrix. The matrix can be any dimensions, not necessarily square.

For example,

[[1,2,3,4],
 [5,1,2,3],
 [6,5,1,2]]
is a Toeplitz matrix, so we should return true, while

[[1,2,3,4],
 [5,1,9,3],
 [6,5,1,2]]
isn’t a Toeplitz matrix, so we should return false.

Constraints:

[time limit] 5000ms
[input] array.array.integer arr
0 ≤ arr.length ≤ 20
0 ≤ arr[i].length ≤ 20
0 ≤ arr[i][j] ≤ 20
[output] boolean
'''
def isToeplitz(arr):
	cols = len(arr[0])
	rows = len(arr)
	
	# intialize starting position to bottom left corner
	r_s = rows - 1
	c_s = 0
	start_positions = rows + cols - 1 # the number of possible starting position
	
	# navigates along the left edge and then the top edge for starting positions from which check left-to-right descending diagonals
	for i in range(start_positions):
		r = r_s
		c = c_s
		last_val = arr[r][c]
			
		# increment down and across
		r += 1
		c += 1

		# navigate down and across from starting position until bounds are reached
		while r < rows and c < cols:
			if last_val != arr[r][c]:
				return False
			last_val = arr[r][c]
			# move one down and across 
			r += 1
			c += 1
		
		r_s -= 1 # move up the start row along the left edge
		# if arrived at top of left edge, move start position one column to the right
		if r_s == -1:
			r_s = 0
			c_s +=1 # move over start column

	return True

# should return True
print (isToeplitz([
	[1,2,3,4],
	[5,1,2,3],
	[6,5,1,2]]))

# should return False
print( isToeplitz([
	[1,2,3,4],
	[5,1,9,3],
	[6,5,1,2]]))