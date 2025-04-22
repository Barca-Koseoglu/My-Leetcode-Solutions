URL: https://leetcode.com/problems/rabbits-in-forest/description/?envType=daily-question&envId=2025-04-20

# 781. Rabbits in Forest

### Runtime: O(n), Space: O(n)

There is a forest with an unknown number of rabbits. We asked n rabbits "How many rabbits have the same color as you?" and collected the answers in an integer array answers where answers[i] is the answer of the ith rabbit.

Given the array answers, return the minimum number of rabbits that could be in the forest.

 
Example 1:

Input: answers = [1,1,2]
Output: 5
Explanation:
The two rabbits that answered "1" could both be the same color, say red.
The rabbit that answered "2" can't be red or the answers would be inconsistent.
Say the rabbit that answered "2" was blue.
Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.

Example 2:

Input: answers = [10,10,10]
Output: 11

 
Constraints:

	1 <= answers.length <= 1000
	0 <= answers[i] < 1000

# Thoughts

A very fun question, albeit a little confusing. What I did was very simple: I used a hash map to count up all the repeating digits in the list (all values plus one because each rabbit who SAID someone else is their color is also counted), 
then I went through the hash map . As I went through, I add to a return variable ((dict[key]//key)+1)*key if dict[key]%key > 0, or else I add the exact same thing without the plus 1. The entire point of this algorithm is to be greedy; if a 
rabbit says there are 20 people like it (including itself), and another rabbit says there are also 20 people like it including itself, then the minimum amount of people there are that are the same color has to be 20. We want the MINIMUM. 
Now, where it gets complicated is when more bunnies say there are x amount of them than the amount that there is, x. So 7 bunnies say there are 3 of them as the same color, including themselves. We can kind of match them up with each other, 
because if some bunny says there are 3 other bunnies like it, assuming two other bunnies also say there are three other bunnies like themselves, to get the minimum, we can just group them together. So of the seven, there's two WHOLE groups of 
three, assuming we try to keep to a minimum, and one bunny saying there are three other like it. This is the +1 case. Since that's the only other bunny left saying there are 3 other ike it, we will have to add that three to our total number of bunnies. 
In the end, we're left with a minimum of 9 bunnies out of the 7 that spoke up. Kind of hard to wrap your head around, but if you think too hard it'll be impossible to understand we only want the minimum, and to get the minimum, we have to 
be greedy.
