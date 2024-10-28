class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        This was a super fun problem. I used something called dynamic programming to solve it. By splitting up the problem into multiple smaller problems, 
        I was able to get the answer quite easily. This was my logic: using two pointers at p1 = nums[-1] and  p2 = nums[-2] (not including the edge case 
        of len(nums) == 1) check if the distance between p1 and p2 is smaller than p1. If it is, make p2 == p1 and p1 -= 1. If the distance is bigger, move 
        on to the number left of p1. If that number is -1, aka outside the array, it would be impossible to get to the end, so we return False. If the while 
        loop exits naturally, so when p1 == -1 but it can reach the nearest number that gets to the end, then it must be possible to get to the end.
        """
        if len(nums) == 1: # edge case
            return True
        p1, p2 = len(nums)-2, len(nums)-1 # pointers as indices
        while p1 > -1:
            if nums[p1] >= p2 - p1: # if nums[p1] can reach nums[p2]
                p2 = p1
                p1 -= 1
            else:
                p1 -= 1
                if p1 == -1: # if it can't reach and p1 is outside the array, then it is False
                    return False
        return True # If it can reach and the loop finishes, then it is True
