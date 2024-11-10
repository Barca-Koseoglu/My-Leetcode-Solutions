class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Return variable is nums, set two pointers to the start and end of the array height and move them right and left respectively using while loops 
        until they are both bigger than 0. Then create a variable called tops that takes the minimum value between both pointers. Move the pointer with the 
        smaller value 1 step inward. Then run a while loop until the left pointer is bigger than or equal to the right pointer. For context, top is the 
        maximum height of the water that can be filled in the tank between the pointers. If the pointer values are the same, set top to one of them and move 
        one inward. If one is smaller than the other, check if it's bigger than top; if it is, set top to it. If it isn't, subtract it from top and add it to
        nums. After that, move it one inward. When the loop finishes, return nums.
        """
        nums = 0
        p1, p2 = 0, len(height)-1
        while height[p1] == 0 and p1 < p2:
            p1 += 1
        while height[p2] == 0 and p2 > p1:
            p2 -= 1
        top = min(height[p1], height[p2])
        if top == height[p1]:
            p1 += 1
        else:
            p2 -= 1
        while p1 < p2:
            if height[p1] == height[p2]:
                top = height[p1]
                p1 += 1
            elif height[p1] < height[p2]:
                if height[p1] < top:
                    nums += top - height[p1]
                else:
                    top = height[p1]
                p1 += 1
            else:
                if height[p2] < top:
                    nums += top - height[p2]
                else:
                    top = height[p2]
                p2 -= 1
        return nums
