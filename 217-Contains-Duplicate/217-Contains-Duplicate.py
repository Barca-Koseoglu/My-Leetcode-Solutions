class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # This solution utilizies a hash set and goes through the list while adding the elements to the set and checking if an element is already in there.
        def length():
            text = set()

            for i in nums:
                if i in text:
                    return True
                text.add(i)

            return False

        # This solution is basically the exact same thing but it uses a built in function to convert the array to a set and return True
        # if the sizes are different (since the set doesn't allow duplicats)
        def short():
            if len(set(nums)) < len(nums):
                return True

            return False
        

        return short()
