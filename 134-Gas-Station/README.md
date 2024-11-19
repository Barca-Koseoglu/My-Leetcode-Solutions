URL: https://leetcode.com/problems/gas-station/description/

# 134. Gas Station

### Time complexity: O(n). Space complexity: O(1)

There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.

 
Example 1:

Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

Example 2:

Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.

 
Constraints:

	n == gas.length == cost.length
	1 <= n <= 105
	0 <= gas[i], cost[i] <= 104

 # Thoughts:
Honestly, this was actually a problem that tripped me up. It's a super unusual problem utilizing a greedy algorithm. I even needed to watch a video from a youtuber called Neetcode to understand it. But the entire thing is much simpler to
understand with these two pieces of knowledge: that the sum of the gas should not be smaller than the sum of the costs, if a solution exists. The second piece is if there is a solution, there can only be one, according to the constraints.
Now, why is it that the sum of the gas, let's call it g, have to be bigger than or equal to the sum of the costs, let's call it c. Think about it this way: if m was greater than n, would that make sense? Put into words, if the total cost 
is more than the gas, it would be impossible to make a full circle around the list since at some point you are guaranteed to have a negative value. This means that if n >= m, there MUST be a solution. Then, how do we find it? Firstly, we 
loop through the length of the arrays. At every point, we update a variable called cost by adding gas[i]-cost[i] to it. Since we know a solution is guaranteed, if total is negative, you cannot go around the list. If that's the case, we set
total back to zero and set our starting point to 1 after the current index. We do this because we know there must be a solution, so we keep upadting the starting point. What if we get to the end of the array? This is what was the hardest 
thing for me to understand. Basically, since we know a solution is guaranteed, and we have already went through those indexes (since we circle through), if our algorithm gets to the end of the array, we can return the starting point 
variable. Again, since we already visited all the other nodes in the array and have a guaranteed answer, we can stop there. Now the more intuitive but inefficient solution is to go through each index of a list of the differences of gas 
and cost, then simulate the entire thing. Every iteration takes an iteration, so the answer would be O(n<sup>2</sup>). Overall, this was a trick question, which I honestly think was interesting but I didn't enjoy solving it much.
