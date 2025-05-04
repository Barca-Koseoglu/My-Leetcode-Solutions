URL: https://leetcode.com/problems/number-of-equivalent-domino-pairs/description/?envType=daily-question&envId=2025-05-04

# 1128. Number of Equivalent Domino Pairs

## Runtime: O(n), Space: O(n)

Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

 
Example 1:

Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1

Example 2:

Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
Output: 3

 
Constraints:

	1 <= dominoes.length <= 4 * 104
	dominoes[i].length == 2
	1 <= dominoes[i][j] <= 9

# Thoughts
This was a very good problem. The main thing about it is the fact that it has to do with combinations. My solution was simple: Iterate through the list and store values in a dict (since the length is 2 for each list I just see if it's in 
the dictionary and if it isn't check the reverse of the tuple and if THAT isn't in it then I add a new one with count 1) and then iterate through the values of the dictionary and use the comination formula simplified to for r=2. There 
was an extremely smart and efficient solution I found while checking the solutions that I wanted to discuss as well. The guy firstly made a list of 0's 100 units long. He then set the return variable to be equal_pairs. Then he NORMALIZED 
everything- this was insanely smart. For a and b of the list he was on (list[0] and list[1] respectively), if a was smaller than or equal, he would multiply a by 10 and add b. otherwise, he would multiply b by ten and add a. Why? This 
guarantees each list has a unique value. After that, he adds on whatever value there was at list_of_zeroes[normalized] to the return variable then adds 1 to that place. He does this end bit to count the pairs. The list of zeroes is 
for the values we have seen before. He adds it to the return variable because that's how many other pairs he can make with the current value. He then adds 1 to that point on the list of zeroes, adding it to the ones already seen because 
it can be paired up with other values in the future. Extremely smart, with time O(n) and space (technically) O(1).
