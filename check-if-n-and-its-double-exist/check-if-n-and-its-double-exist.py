class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if arr.count(0) > 1:
            return True
        for i in arr:
            if i*2 in arr and i != 0:
                return True
                
        