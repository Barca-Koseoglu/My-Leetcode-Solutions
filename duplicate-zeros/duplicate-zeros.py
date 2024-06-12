class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        indexes = []
        for i in range(len(arr)):
            if i < len(arr)-len(indexes):
                if arr[i] == 0:
                    indexes.append(i)
        extra = 0
        for i in range(len(indexes)):
            indexes[i] += extra
            del arr[-1]
            arr.insert(indexes[i], 0)
            extra += 1
            
            
                
                
                
                