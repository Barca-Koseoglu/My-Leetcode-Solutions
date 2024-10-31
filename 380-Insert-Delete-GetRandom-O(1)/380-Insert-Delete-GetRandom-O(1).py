import random
"""
This class uses a list and a dictionary. The dictionary allows the insertion and deletion of elements to be in O(1) and the list is used to get a random value utilizing .choice() from the random module. The dicitonary stores the values 
as keys and their index in the list as values, which allows insertion and deletion for the list to be in O(1) time as well.
"""
class RandomizedSet:

    def __init__(self):
        self.rand = []
        self.vals = {}

    def insert(self, val: int) -> bool: # append to the list and make a key in the dict
        if val in self.vals:
            return False
        self.rand.append(val)
        self.vals[val] = len(self.rand)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.vals:
            return False
        self.rand[self.vals[val]] = self.rand[-1] # use dict to access index in the list and switch values with the last value in the list
        self.vals[self.rand[-1]] = self.vals[val] # switch dict values
        self.rand.pop()
        del self.vals[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.rand)
