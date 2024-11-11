URL: https://leetcode.com/problems/add-two-numbers-ii/description/?envType=study-plan-v2&envId=programming-skills

# 445. Add Two Numbers II --- Medium

### Time complexity: O(n), Space complexity: O(n)

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 
Example 1:

Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]

Example 2:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]

Example 3:

Input: l1 = [0], l2 = [0]
Output: [0]

 
Constraints:

	The number of nodes in each linked list is in the range [1, 100].
	0 <= Node.val <= 9
	It is guaranteed that the list represents a number that does not have leading zeros.

 
Follow up: Could you solve it without reversing the input lists?

# Thoughts:
If you decide to reverse the lists, then you gotta go through a bunch of node adding and checking the lengths and carrying the ones and a bunch of mumbo jumbo. That is definetly a valid solution, but I took a different approach. I just 
iterated through both lists and turned them into strings. Then I turned them into integers, added them, and turned them into strings again. Then I just made another linked list out of the string.
