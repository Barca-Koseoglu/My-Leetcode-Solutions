class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        chicken = {}
        answers = [x+1 for x in answers]
        for i in answers:
            if i in chicken:
                chicken[i] += 1
            else:
                chicken[i] = 1
        ans = 0
        if 1 in chicken:
            ans += chicken[1]
            del chicken[1]
        for i in chicken:
            ans += (1+chicken[i]//i)*i if chicken[i] % i != 0 else i * (chicken[i] // i)
        return ans
