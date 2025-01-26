URL: https://leetcode.com/problems/candy/description/?envType=study-plan-v2&envId=top-interview-150

# 135. Candy

## Time complexity: O(n). Space complexity: O(n)

There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

	Each child must have at least one candy.
	Children with a higher rating get more candies than their neighbors.

Return the minimum number of candies you need to have to distribute the candies to the children.

 
Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.

 
Constraints:

	n == ratings.length
	1 <= n <= 2 * 104
	0 <= ratings[i] <= 2 * 104

# Thoughts:
This is a HORRIBLY worded problem. I was stuck on this problem for an ENTIRE 4 hours, wondering what I was getting wrong. Turns out, I thought array[i] had to be bigger than the COMBINED candy of the neightbors of it assuming it's rating 
is bigger than both of it's neighbors.After figuring out that it wasn't, it was easy as cake. Firstly, every child get's candy, so I created a seperate list named candy that was len(ratings) long and all set to 1. Basically, going from 
left to right first, I check every kid i so that if i-1 is bigger, candy[i] = candy[i-1]+1. This guarantees that each element i that's bigger than another element i-1 has more candy than it. I didn't do this the opposite way, starting from 
i=0 and checking i+1 and continuing because imagine a list [5,4,3,2,1]. If we check the 0th and 1st position, with our i at 0, and see that it's bigger, we know that the candy array, [1,1,1,1,1], will increase the first position by 1, since 
our algorithm is greedy, making it [2,1,1,1,1]. But now we move our i to 2 and check 3. We see that it's bigger, so we increase it by the smallest value we can, 1: [2,2,1,1,1]. But wait, isn't 1 supposed to be bigger than 0? Yes, but this way 
doesn't account for it. So, in order to account for each change, we check the place we were at, since it would have an updated value based on the values before it. Kind of hard to explain, but if we do that same thing the other way as well, then 
sum up candy, we get our answer. A very good problem, ruined by it's horrendous wording.
