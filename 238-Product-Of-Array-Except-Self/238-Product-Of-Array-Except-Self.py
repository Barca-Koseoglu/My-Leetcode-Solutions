class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        This is extremely simple if you use some basic math. First, I went over the array to count the zeros and to calculate the product 
        of the non-zero elements. If the entire array was zeros, then just return the array. If there is more than 1 zero, then just return an 
        array the size of the original array with just zeros in it. If there is one or no zeros, then loop through the original list. If i, the 
        iteration variable, is 0, append the product to the return variable. if there is a zero and i is an int, append 0. If there isn't a zero and 
        i is an int, append the product times i^-1, since this divides the product without using the division operator.
        """
        ans = [] # return array
        prod = 1 # product
        zeros = 0
        for i in nums: # to see if array has a zero and take product of non-zero ints
            if i == 0:
                zeros += 1
                if zeros > 1:
                    return [0]*len(nums)
            else:
                prod *= i
        for i in nums:
            if i == 0: # dividing by zero is impossible, so just put in the product
                ans.append(prod)
            elif zeros == 1: # then put in 0 cause it will be multiplied by 0
                ans.append(0)
            else: # normal case, just multiply product with i**-1
                ans.append(int(prod*(i**-1))) # ps dont forget to convert to int since the act of dividing turns it into a float
        return ans
