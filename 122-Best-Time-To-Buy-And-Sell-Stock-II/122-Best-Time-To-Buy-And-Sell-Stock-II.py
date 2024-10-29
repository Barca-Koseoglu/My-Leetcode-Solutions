class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        What I did was enumerate through the list and whenever the number in front of the current number is bigger than it, I just subtracted them and added the value to my return variable.
        """
        total = 0 # return var
        for i in range(len(prices)-1): 
            if prices[i] < prices[i+1]: # checks if number after it is bigger
                total += prices[i+1] - prices[i] # adds difference to return var
        return total        
