class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Dictionary solution
        def dict_sol():
            counts, ans = {}, []

            for i in nums:
                if i in counts:
                    counts[i] += 1
                else:
                    counts[i] = 1

                if counts[i] > len(nums)//3 and i not in ans:
                    ans.append(i)
            
            return ans

        # Boyer-Moore Algorithm solution. Solution uses dictionaries as a more general way to find elements more than n/k where k is a constant
        def boyer_moore():
            two = defaultdict(int)

            for i in nums:
                two[i] += 1

                if len(two) == 3:
                    new_count = defaultdict(int)
                    for i, a in two.items():
                        if a > 1:
                            new_count[i] = a - 1
                    two = new_count
            
            ans = []
          
            for n in two:
                if nums.count(n) > len(nums)//3:
                    ans.append(n)
            
            return ans

        return boyer_moore()
