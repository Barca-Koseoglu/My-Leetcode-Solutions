#Thinking notes:
"""
given x pairs of parentheses, make a function that generates all combinations of WELL FORMED PARENTHESES


output: list of str


x pairs: each str gotta be length 2x. x of each openeing and closing parantheses

"generates" so use recursion? caching for that too

combinations: dealing with lots of number, maybe something about well formed parantheses has a pattern or rule to shorten


well-formed parantheses: all parentheses gotta have an opening and closing, overlap not possible! since it gotta have [n(] == [n)]

constraints between 1 and 8, so length of individual strings for checking is O(1). recursion itself gives O(n). space is O(n!)???

psuedocode idea: do recursion. No need to actually check constantly if it's well formed. base case, length of the 
str is n*2, so return [str]. NUM var is to check if parantheses match. 0 mean all of the are matching. adding an open 
parantheses makes it +1, -1 if adding a closed parantheses. can only go up to var n until it must subtract to balance out 
open and closed.

recur(str, num):
    if length == n:
        return [str]
    elif num == 0:
        return recur(str+'(', 1))
    elif num < n:
        return recur(str+'(', num+1) + recur(str+')', num-1)
    else:
        return recur(str+')', num-1)

slight problems, but will fix during coding
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #first
        """
        @cache
        def recur(str_comb, num):
            if len(str_comb) == 2*n:
                if num == 0:
                    return [str_comb]
                else:
                    return []
            elif num == 0:
                return recur(str_comb + '(', 1)
            elif num < n:
                return recur(str_comb + '(', num+1) + recur(str_comb + ')', num-1)
            else:
                return recur(str_comb + ')', num-1)

        return recur('', 0)
        """
        #shortened
        def recur(str_comb):
            a = str_comb.count('(')
            b = str_comb.count(')')
            if len(str_comb) == 2*n:
                return [str_comb]
            elif a == b:
                return recur(str_comb + '(')
            elif a - b < n:
                if a == n:
                    return recur(str_comb + ')')
                return recur(str_comb + '(') + recur(str_comb + ')')
            else:
                return recur(str_comb + ')')

        return recur('')
        
