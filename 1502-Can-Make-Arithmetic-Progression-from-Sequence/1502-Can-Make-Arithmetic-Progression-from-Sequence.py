class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        """
        First sort the array and find the difference of the first and second elements. Then go throught the array except the final value to see if the 
        difference plus the value of the index is equal to the next element. If it isn't return False. After exiting the for loop, return True.
        """
        arr.sort()
        val = arr[1] - arr[0]
        for i in range(len(arr)-1):
            if arr[i] + val != arr[i+1]:
                return False
        return True
