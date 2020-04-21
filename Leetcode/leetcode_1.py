# PROBLEM
'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 15, 17], target = 24,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]

edge cases: negative nums, zero values, identical values (there is only one solution)
'''
#### Solution 1 using hashing ####
# time = O(N) bc we have loop through array once but as we go through we are inserting or looking up from dict which is O(1) thanks to magic of hashing so these operations don't affect big-O
# space = O(1) since we have a most one call on stack
def getTargetPair1(nums, target):
	diff_dict = {}
	for i in range(len(nums)):
		diff = target - nums[i]
		match_idx = diff_dict.get(nums[i])
		if match_idx == None:
			diff_dict[diff] = i
		else:
			return [match_idx, i]

#### Solution 2 given ascending sorted input####
# time = O(N) bc we have loop through array once
# space = O(1) since no extra data structure is used and at most one call is on the stack
def getTargetPair2(nums, target):
	# start at outer edges
	l = 0
	r = len(nums) - 1
	while l < r:
		# print('comparing l: ' + str(nums[l]) + ' r: ' + str(nums[r]))
		total = nums[l] + nums[r] 
		if total == target:
			return [l, r]
		elif total > target:
			r -= 1
		else:
			l += 1

nums1  = [2, 7, 15, 17]
target = 24

print(getTargetPair1(nums1, target))
print(getTargetPair2(nums1, target))