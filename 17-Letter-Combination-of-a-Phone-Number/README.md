URL: https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/?envType=study-plan-v2&envId=top-100-liked

# 17. Letter Combinations of a Phone Number

Time: 0 ms, Memory: 16.74 MB

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

 
Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:

Input: digits = ""
Output: []

Example 3:

Input: digits = "2"
Output: ["a","b","c"]

 
Constraints:

	0 <= digits.length <= 4
	digits[i] is a digit in the range ['2', '9'].

 # Thoughts:
 I really like this problem because it uses recursion and backtracking. What we have to do is find every combination of letters from the numbers. So 23 would have nine, ad ae af bd be bf cd ce cf. The first thing I thought about was to map 
 these numbers to their letters and use a function to recursively go through a combination then backtrack to another combination. so looking at 23, we would start with 'a' then go to the first letter of three which would be 'd'. then we go 
 back to 'a' and take the second letter of three, 'e', then the third, d, then backtrack to the beginning where we had nothing and use 'b', and so on and so forth. I used a function to do this. It would take the index value of the string of 
 numbers and the current combination of letters. If the index value is bigger than the length of the numbers string, then we would stop that recursion. If it isn't we iterate through the index's letters from the dictionary and add the 
 current iteration of the letter onto the current letter combination. Then we run the function recusrively with the next index and the current combination until it exits. After it does, we chek if the combination is the correct length then 
 add it to the return variable. Finally we delete the latest letter in the combination to place in different letters in the same places. Finally we run the function and return the combinations.
