URL: https://leetcode.com/problems/can-place-flowers/description/?envType=study-plan-v2&envId=leetcode-75

# 605. Can Place Flowers

Time: 10 ms, Memory: 17.01 MB

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 
Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

 
Constraints:

	1 <= flowerbed.length <= 2 * 104
	flowerbed[i] is 0 or 1.
	There are no two adjacent flowers in flowerbed.
	0 <= n <= flowerbed.length

# Thoughts:
I made the code much slower and longer than it should have been, but in my opinion it's more understandable this way. Also I was feeling a bit lazy today. Anyways, it wasn't hard at all. If the length of the list was 1, then we would just see 
if it was 0 and if "n" was 1 or 0, and we return False otherwise. Then, we make a variable called count that keeps track of how many flowers could be planted. We enumerate throught the list; if we're at the start or end of the list (and 
the number we're on is 0), we only check the number after or before, respectively. If those numbers are 0, then we add 1 to count and change the number from 0 to 1, but we don't have to do this at the end since it'll just be a useless extra 
operation. If we're somewhere else in the list, then we check both the number before and after us if we're zero. If we are zero and both those numbers are zero, we add 1 to count and change that part of the list from 0 to 1. After every 
iteration of the list, we check if count is bigger than or equal to n, and if it is we just simply return True. If we get out of the list, that means we couldn't plant enough flowers and we return False. Overall, it was very easy to do.
