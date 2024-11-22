class MyHashSet:

    def __init__(self):
        self.contain = [[] for x in range(1000)]
        
    def add(self, key: int) -> None:
        put = key%1000
        if key not in self.contain[put]:
            self.contain[put].append(key)
            
    def remove(self, key: int) -> None:
        put = key%1000
        for i, x in enumerate(self.contain[put]):
            if x == key:
                del self.contain[put][i]
                
    def contains(self, key: int) -> bool:
        put = key%1000
        if key in self.contain[put]:
            return True
        return False
        
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
