class Solution:
    def judgeCircle(self, moves: str) -> bool:
        """
        Make two vars x and y representing coordinate points. Then iterate through moves. If moves[i] == D or U, increase or decrease y by 1 respectively, 
        and do the same for x when moves[i] == L or R. If x an y are 0 after iterating, return True, else return False.
        """
        x, y = 0, 0
        for i in moves:
            if i == "U":
                y += 1
            elif i == "D":
                y -= 1
            elif i == "L":
                x -= 1
            else:
                x += 1
        if x == 0 and y == 0:
            return True
        return False
