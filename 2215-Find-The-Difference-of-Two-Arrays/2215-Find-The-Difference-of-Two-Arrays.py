class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        """
        Turn the lists into sets to get rid of duplicates. Then iterate over the first set and see if there is a number that doesn't appear in the second 
        set. If there is, append it onto the return variable ans1. Then do the same thing but iterate over the other set and append onto the ans2 return 
        variable. Then return the answers.
        """
        nums1, nums2 = set(nums1), set(nums2)
        ans1, ans2 = [], []
        for i in nums1:
            if i not in nums2:
                ans1.append(i)
        for i in nums2:
            if i not in nums1:
                ans2.append(i)
        return [ans1, ans2]
