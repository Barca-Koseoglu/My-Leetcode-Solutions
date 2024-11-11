URL: https://leetcode.com/problems/lemonade-change/description/?envType=study-plan-v2&envId=programming-skills

# 860. Lemonade Change --- Easy

### Time Complexity: O(n), Space Complexity: O(1)

At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

Note that you do not have any change in hand at first.

Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.

 
Example 1:

Input: bills = [5,5,5,10,20]
Output: true
Explanation: 
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change, we output true.

Example 2:

Input: bills = [5,5,10,10,20]
Output: false
Explanation: 
From the first two customers in order, we collect two $5 bills.
For the next two customers in order, we collect a $10 bill and give back a $5 bill.
For the last customer, we can not give the change of $15 back because we only have two $10 bills.
Since not every customer received the correct change, the answer is false.

 
Constraints:

	1 <= bills.length <= 105
	bills[i] is either 5, 10, or 20.

# Thoughts:
It's literally just following instructions systematically. We just keep track of our fives and tens with two variables. We don't keep track of the twenties we get since they can't be given for change due to the constraints. If we get a 20, 
though, we first see if we can give a five and a ten for change. If not, we check if we can give three fives. If not, we return False. This works out since if we save more fives to give more change it the time calls for it. If we try to save 
then tens, we might not be able to give change once we recieve the tens.
