URL: https://leetcode.com/problems/zigzag-conversion/description/?envType=study-plan-v2&envId=top-interview-150

# 6. Zigzag Conversion

### Runtime: O(n), Space: O(n)

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

 
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:

Input: s = "A", numRows = 1
Output: "A"

 
Constraints:

	1 <= s.length <= 1000
	s consists of English letters (lower-case and upper-case), ',' and '.'.
	1 <= numRows <= 1000

# Thoughts

I avoided this problem for a very long time, mainly because the question desription was very complicated and scary-looking. After checking it out again, though, it's just using a list of strings to store the rows and concatenating the 
letters one by one, 'turning around' when you get to one end or another using a true or false variable and determining where it goes using a pointer. I overcomplicated this for a while using the modulus operator but in reality it's a very 
simple problem.
