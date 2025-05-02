class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        new_dominoes = ''
        p1, p2 = 0, 0
        while p1 < len(dominoes):
            if dominoes[p1] == 'R':
                p2 = p1 + 1
                while p2 != len(dominoes):
                    if dominoes[p2] == 'R':
                        new_dominoes += 'R'*(p2-p1)
                        p1 = p2
                        break
                    elif dominoes[p2] == 'L':
                        if (p2-p1)%2 == 0:
                            new_dominoes += 'R'*((p2-p1)//2) + '.' + 'L'*(((p2-p1)//2))
                        else:
                            new_dominoes += 'R'*((p2-p1+1)//2) + 'L'*(((p2-p1+1)//2))
                        p1 = p2 + 1
                        break
                    p2 += 1
                if p2 == len(dominoes):
                    new_dominoes += 'R'*(p2-p1)
                    break   
            elif dominoes[p1] == 'L':
                p2 = p1 - 1
                while p2 > -1 and dominoes[p2] != 'L':
                    p2 -= 1
                if p2 == -1:
                    new_dominoes = 'L'*(p1-p2)
                else:
                    if p1-p2 != 1:
                        new_dominoes = new_dominoes[:-(p1-p2-1)]
                    new_dominoes += 'L'*(p1-p2)
                p1 += 1
            else:
                p1 += 1
                new_dominoes += '.'
                
        return new_dominoes
