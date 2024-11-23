URL: https://leetcode.com/problems/climbing-stairs/description/

# 70. Climbing Stairs

### Time complexity: O(n) where n is the given variable. Space complexity: O(1)

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 
Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

 
Constraints:

	1 <= n <= 45

# Thoughts:
Probably one of the best dynamic programming questions. The way to solve this is hard to figure out at first but it's very simple. Imagine the stairs take 5 steps to reach the top. Now imagine you're at the fourth step. How many ways are there
to get to the top? Obviously, one. Now imagine you're at the third step. Now how manyways are there to get to the top? You could take two steps and get to the top, so that's one way. But you can also take one step onto the fourth step, and 
since we know there's only one way to get from the fourth step to the top, we add one to the number of ways, so from the third step, there are 2 ways to get to the top. Now, let's look at the second step. You can either move one step, which 
takes us to the third step where there are two ways to get to the top, or you can take two steps and land on the fourth step, which takes only one step to get to the top. Adding ways together, we get three different ways. This pattern continues on. 
In the case of this stairway, on the first step there are second step + third step ways, so 5 ways, and on at the start, there are first step + second step, so 8 In total there are eight ways. This pattern is called the **Fibonacci sequence**. 
Using dynamic programming and the pattern of the Fibonacci sequence, this question is solved very efficiently. 
