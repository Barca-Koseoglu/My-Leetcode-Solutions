class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        for i in range(len(arr)-1,-1,-1):
            if i == len(arr)-1:
                biggest = arr[i]
                continue
            if arr[i] > biggest:
                save = biggest
                biggest = arr[i]
                arr[i] = save
            else:
                arr[i] = biggest
        arr[-1] = -1
        return arr