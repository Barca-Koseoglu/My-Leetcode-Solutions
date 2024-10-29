class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Personally, I think my code is really messy here. It utilizes a greedy algorithm of O(N) time and O(1) space complexity. 
        Basically, In order to find the fastest way to get to the end, I started from the beginning and found the biggest number I could jump 
        to. Since it's guaranteed that I will be able to make it to the end, if I constantly find the largest number in the space I can jump,
        I will make it to the end in the shortest way possible. So I used three variables: count (counts the jumps I have done, starts at 1 but
        has an edge case when the length of nums is equal to 0), top (the farthest I can reach . If it goes past len(nums)-1, that means I have succesfully
        reached the end), and p1 (pointer that starts at 0). I made a while loop that has a for loop in it that checks for the biggest number that surpasses
        "top". After iterating through the numbers, it adds 1 to count and adds on the extra length to the "top" variable and starts again from the end 
        of the p1 range.
        """
        if len(nums) == 1: # edge case
            return 0
        count, top, p1, = 1, nums[0], 0 
        while top < len(nums)-1:
            store = 0
            for i in range(p1+1, top + 1): # checking the entire distance of the jump
                if i + nums[i] - top > store: # if it get closer to the end, it is better
                    store = i + nums[i] - top
            p1 += nums[p1]
            top += store
            count += 1
        return count
