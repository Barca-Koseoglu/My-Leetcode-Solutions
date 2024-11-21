URL: https://leetcode.com/problems/merge-sorted-array/description/

# 88. Merge Sorted Array

### Time complexity: O(n+m) for n == len(nums1) and m == len(nums)2. Space complexity: O(1) since we sort in-place.

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 
Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

 
Constraints:

	nums1.length == m + n
	nums2.length == n
	0 <= m, n <= 200
	1 <= m + n <= 200
	-109 <= nums1[i], nums2[j] <= 109

 
Follow up: Can you come up with an algorithm that runs in O(m + n) time?

# Thoughts:
For some reason, this question caused me to struggle a lot. I solved it a few months ago, but I kind of cheated by using .sort(), so I decided to do this one more efficiently. When sorting two sorted lists, I first think to make an array and iterate through both of them with pointers step by step **starting from the beginning** and keep going till both of them have reached the end. The thing that makes this question unique is that in order to solve it in optimal time, you have to start from the ends, aka the largest numbers of both arrays. Then you have to create a pointer for the extra space which could me marker = n+m-1 (or iterate backwards through the length of nums1, whatever you prefer), then you go through them all one by one. I was wondering how I could go from the start, but the trick was found in the end. A great problem honestly, maybe should be medium rated though.
