class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = {}
        for i in dominoes:
            if tuple(i) in count:
                count[tuple(i)] += 1
            elif tuple(reversed(i)) in count:
                count[tuple(reversed(i))] += 1
            else:
                count[tuple(i)] = 1

        ret = 0
        for i in count:
            ret += count[i]*(count[i]-1) // 2

        return ret
