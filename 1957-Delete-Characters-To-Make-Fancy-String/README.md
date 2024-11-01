URL: https://leetcode.com/problems/delete-characters-to-make-fancy-string/description/?envType=daily-question&envId=2024-11-01

# 1957. Delete Characters to Make Fancy String

Time: 514 ms, Memory: 18.22 MB

A fancy string is a string where no three consecutive characters are equal.

Given a string s, delete the minimum possible number of characters from s to make it fancy.

Return the final string after the deletion. It can be shown that the answer will always be unique.

 
Example 1:

Input: s = "leeetcode"
Output: "leetcode"
Explanation:
Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode".

Example 2:

Input: s = "aaabaaaa"
Output: "aabaa"
Explanation:
Remove an 'a' from the first group of 'a's to create "aabaaaa".
Remove two 'a's from the second group of 'a's to create "aabaa".
No three consecutive characters are equal, so return "aabaa".

Example 3:

Input: s = "aab"
Output: "aab"
Explanation: No three consecutive characters are equal, so return "aab".

 
Constraints:

	1 <= s.length <= 105
	s consists only of lowercase English letters.

 # Thoughts:
 I used the sliding window technique to solve this problem. The solution was slow, but it worked. If the length of the list is smaller than 3, just return the list. Otherwise, create three pointers p1, p2, and p3 as 0, 1, and 2 
 respectively. These will go through the entire list. Then make a while loop until p3 is equal to the length of the list. As we go through, we want to append the correct parts onto our return variable ans. If the values in indices 
 p1, p2 and p3 are not the same, add on the value in p1 to and. If they are the same, don't add anything. Then, just add 1 to each pointer. After exiting the loop, return ans with the values from p1 and p2 concatenated on it in that 
 order. We need to do this because it only adds the values for p1, and after the loop finishes list[p1] and list[p2] are both list[-2] and list[-1] respectively.
