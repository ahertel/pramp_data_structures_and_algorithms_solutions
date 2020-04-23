'''
n = num of ints
O(n^2)

O(2N) -> O(N)

BCR O(N)

sorting and/or searching:
10,8,2

hashing?:

O(N) space, O(N) time?
running product from each end
[8, 10, 2]
l = [8,80,160]
r = [160,20,2]
s = [20, 16, 80]

[2, 7, 3, 4]
l = [2,14,42,128]
r = [128,84,12,4]
s = [84, 24, 56, 42]

s[1] = l[0] * r[2] aka 2 * 12
s[2] = l[1] * r[3] aka 4 * 14

s[0] = r[1]
s[len-1] = l[2]


'''

def array_of_array_products2(arr):
	length = len(arr)
	prod_arr = [1 for i in arr]
	for i in range(1, length, 1):
		prod_arr[i] = prod_arr[i-1] * arr[i-1]
	print(prod_arr)
	prod_arr = [1 for i in arr]
	for i in range(length-2, -1, -1):
		prod_arr[i] = prod_arr[i+1] * arr[i+1]
	print(prod_arr)

print(array_of_array_products2([2, 3, 4, 5]))


# time: O(3n) -> O(n)