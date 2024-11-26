class Solution:
    def firstUniqChar(self, s: str) -> int:
        #This solution utilizes a dictionary to store the counts of values and return the first unique character.
        def normal():
            storage = {}

            for i in s:
                if i not in storage:
                    storage[i] = 1
                else:
                    storage[i] += 1

            for i, x in enumerate(s):
                if storage[x] == 1:
                    return i

            return -1
        
        # This solution is similar to the one above except it iterates over the dictionary instead of the string.
        def memorable_dict():
            storage = {}

            for i, a in enumerate(s):
                if a not in storage:
                    storage[a] = [1, i]
                else:
                    storage[a][0] += 1
            
            for i in storage:
                if storage[i][0] == 1:
                    return storage[i][1]
            
            return -1

        return memorable_dict()
                
