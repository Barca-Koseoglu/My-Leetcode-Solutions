class Solution:
    def countLargestGroup(self, n: int) -> int:
        check = {}
        for i in range(1, n+1):
            group = sum([int(x) for x in str(i)])
            if group in check:
                check[group] += 1
            else:
                check[group] = 1
        big = 0
        for i in check:
            big = max(big, check[i])
        ans = 0
        for i in check:
            if check[i] == big:
                ans += 1
        return ans
