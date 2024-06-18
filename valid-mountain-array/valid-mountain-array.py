class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        down = False
        big = max(arr)
        if big == arr[-1] or big == arr[0]:
            return False
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1]:
                return False
            if arr[i] == big:
                down = True
            if down:
                if arr[i] < arr[i+1]:
                    return False
            else:
                if arr[i] > arr[i+1]:
                    return False
        return True
                
            
            