# Leetcode
# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

	def printLL(self):
		current = self
		while current != None:
			print(str(current.val) + ', ', end=' ')
			current = current.next
		print()

class Solution:
	def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

		carry = 0

		head = None
		curr = head
		while (l1 or l2 or carry) :

			l1_v = l2_v = 0
			if l1 != None:
				l1_v = l1.val
				l1 = l1.next

			if l2 != None:
				l2_v = l2.val
				l2 = l2.next
			
			sum_val = l1_v + l2_v + carry
			rem = ((sum_val) % 10)
			carry = int((sum_val) / 10)
			
			if head == None:
				head = ListNode(rem)
				curr = head
			else:
				curr.next = ListNode(rem)
				curr = curr.next

		return head


# Test Cases 
s = Solution()

# create LLs
head1 = ListNode(2)
curr = head1
curr.next = ListNode(4)
curr = curr.next
curr.next = ListNode(3)

head2 = ListNode(5)
curr = head2
curr.next = ListNode(6)
curr = curr.next
curr.next = ListNode(4)

# Test 1: equal size ints
result1 = s.addTwoNumbers(l1= head1, l2= head2)
result1.printLL()


# Test 2: one num test
result2 = s.addTwoNumbers(l1= ListNode(2), l2= ListNode(5))
result2.printLL()

# Test 3: unequal size ints test
result3 = s.addTwoNumbers(l1= head1.next, l2= head2)
result3.printLL()

# Test 4: last num is > 9
head4 = ListNode(9)
head4.next = ListNode(9)
result4 = s.addTwoNumbers(l1= ListNode(1), l2= head4)

result4.printLL()