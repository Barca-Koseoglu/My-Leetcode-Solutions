class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        """
        Make two variable called five and ten to store the fives and tens. Then iterate through the list. For i == 5, add 1 to five. For i == 10, if you have 
        at least 1 in five then add 1 to ten and subtract 1 from five. Else return False. If i == 20, see if you have a ten. if yes, see if you have a five. 
        If yes then subtract 1 from ten and five. If not return false. If you don't have a 10, check if you have at lest 3 fives. If you do, subtract 3 from 
        five. Otherwise return False.
        """
        five, ten = 0, 0
        for i in bills:
            if i == 5:
                five += 1
            elif i == 10:
                if five == 0:
                    return False
                five -= 1
                ten += 1
            else:
                if ten == 0:
                    if five > 2:
                        five -= 3
                    else:
                        return False
                elif five > 0:
                    five -= 1
                    ten -= 1
                else:
                    return False
        return True
