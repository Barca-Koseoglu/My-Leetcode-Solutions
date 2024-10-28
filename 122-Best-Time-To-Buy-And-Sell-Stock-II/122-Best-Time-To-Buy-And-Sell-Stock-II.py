class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        It took me a while to get this solution. At first, I thought of finding the maximum and minimum values and subtracting them, but 
        later I realized that was the solution to the first question. After thinking about it, I figured out that if i buy and sell every time a profit 
        was to be made, I could get the answer. It reminds me of a greedy algorithm. So what I did was enumerate thtough the list and whenever the number in 
        front of the current number is bigger than it, I just subtracted them and added the value to my return variable, total.
        """
        total = 0 # return var
        for i in range(len(prices)-1): 
            if prices[i] < prices[i+1]: # checks if number after it is bigger
                total += prices[i+1] - prices[i] # adds difference to return var
        return total        
