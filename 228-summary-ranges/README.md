URL: https://leetcode.com/problems/summary-ranges/description/?envType=problem-list-v2&envId=array

#228. Summary Ranges

### Runtime: O(n), Space: O(n)

You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

	"a->b" if a != b
	"a" if a == b

 
Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"

 
Constraints:

	0 <= nums.length <= 20
	-231 <= nums[i] <= 231 - 1
	All the values of nums are unique.
	nums is sorted in ascending order.

# Thoughts:

A very fun little problem to do, especially as a warm up. The whole logic was to keep a holder variable and then loop through the list to see if the DISTANCE between holder and i is the same as the DISTANCE between nums[holder] and 
nums[i]. If it is, then all the integers between are consecutive integers and we can keep going. If it isn't, we check to see if i-1 == holder, and if it is we just append str(nums[holder]) onto the return list. If they have distance between 
each other, we simply append the f-string f'{nums[holder]}->{nums[i-1]}'. Then we set holder to i and keep going. At the end of the iterations, it won't run the code for the last bit of iterations, so I decided to just copy the entire bit 
of code and replace i with len(nums). Also, the only edge case is [], and for that I just return [].
