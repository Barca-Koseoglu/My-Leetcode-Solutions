URL: https://leetcode.com/problems/push-dominoes/description/?envType=daily-question&envId=2025-05-02

# 838. Push Dominoes

### Runtime: O(n), Space: O(n)

There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

You are given a string dominoes representing the initial state where:

	dominoes[i] = 'L', if the ith domino has been pushed to the left,
	dominoes[i] = 'R', if the ith domino has been pushed to the right, and
	dominoes[i] = '.', if the ith domino has not been pushed.

Return a string representing the final state.

 
Example 1:

Input: dominoes = "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.

Example 2:

Input: dominoes = ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."

 
Constraints:

	n == dominoes.length
	1 <= n <= 105
	dominoes[i] is either 'L', 'R', or '.'.

# Thoughts:

A VERY fun problem that's based on playing with two pointers and giving specific instructions. It was technically very easy since the most complicated part of the program is "if p1 finds R, send out p2 to find L. If p2 finds R, add a 
line of length p2 - p1 which is just R to the return variable and set p1 to R (in case L pops up afterwards)." It is very difficult to just explain it, but it's technical and detailed instructions. If you find L and p2 goes left 
until you find another L, then delete that last little portions and replace it with a portion of all L's. If you found R and p2 found L then if the distance between the pointers is positive, leave the middle period and replace the left 
and right side of it rith R's and L's respectively. Lots of very vivid details which makes it look scary when in reality it really isn't that bad.
