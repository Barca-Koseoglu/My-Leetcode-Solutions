class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        Create a variable to keep track of how many flowers can be planted, called count. Enumerate through flowerbed; if you're at the start or end of the 
        list, check the next and the previous number respectively. If they're zero, add 1 to count and change the number from 0 to 1 at the start. There's 
        no need to change the number in the list at the end. If you're somewhere else in the list, check both the numbers before and after it. If they're 
        both zero, change the number in the list and add 1 to count. If count is bigger than or equal to "n", then reutrn true. Otherwise, return False. Edge 
        case deals with if the list is only 1 number long.
        """
        if len(flowerbed) == 1: # edge case, annoyingly long
            if n == 0:
                return True
            elif flowerbed[0] == 0 and n == 1:
                return True
            else:
                return False
        count = 0
        for i, a in enumerate(flowerbed): # actual meat of the code
            if i == 0:
                if a == 0 and flowerbed[i + 1] == 0:
                    count += 1
                    flowerbed[i] = 1
            elif i == len(flowerbed)-1:
                if a == 0 and flowerbed[i - 1] == 0:
                    count += 1 # we don't change the number in the list since this would be the final iteration of the loop
            else:
                if a == 0:
                    if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                        count += 1
                        flowerbed[i] = 1
            if count >= n:
                return True
        return False
