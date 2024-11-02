URL: https://leetcode.com/problems/circular-sentence/description/?envType=daily-question&envId=2024-11-02

# 2490. Circular Sentence

Time: 4 ms, Memory: 16.42 MB

A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

	For example, "Hello World", "HELLO", "hello world hello world" are all sentences.

Words consist of only uppercase and lowercase English letters. Uppercase and lowercase English letters are considered different.

A sentence is circular if:

	The last character of a word is equal to the first character of the next word.
	The last character of the last word is equal to the first character of the first word.

For example, "leetcode exercises sound delightful", "eetcode", "leetcode eats soul" are all circular sentences. However, "Leetcode is cool", "happy Leetcode", "Leetcode" and "I like Leetcode" are not circular sentences.

Given a string sentence, return true if it is circular. Otherwise, return false.

 
Example 1:

Input: sentence = "leetcode exercises sound delightful"
Output: true
Explanation: The words in sentence are ["leetcode", "exercises", "sound", "delightful"].
- leetcode's last character is equal to exercises's first character.
- exercises's last character is equal to sound's first character.
- sound's last character is equal to delightful's first character.
- delightful's last character is equal to leetcode's first character.
The sentence is circular.

Example 2:

Input: sentence = "eetcode"
Output: true
Explanation: The words in sentence are ["eetcode"].
- eetcode's last character is equal to eetcode's first character.
The sentence is circular.

Example 3:

Input: sentence = "Leetcode is cool"
Output: false
Explanation: The words in sentence are ["Leetcode", "is", "cool"].
- Leetcode's last character is not equal to is's first character.
The sentence is not circular.

 
Constraints:

	1 <= sentence.length <= 500
	sentence consist of only lowercase and uppercase English letters and spaces.
	The words in sentence are separated by a single space.
	There are no leading or trailing spaces.

 # Thoughts:
 This was an extremely easy problem. Firstly, I checked to see if the start and end of the string were equal. If they weren't immediately return False because it wouldn't be a circular string. Then, split the string into a list of just 
 the words. Then iterate through all but the last word, checking if the end of the first word matches the start of the second word. If it doesn't return False. If the loop finishes, return True. By the way, this is case specific, so if 
 string[0] is D and string[-1] is d, we would return False.
