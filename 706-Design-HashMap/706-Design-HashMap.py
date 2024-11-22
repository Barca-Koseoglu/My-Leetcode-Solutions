class MyHashMap:

    def __init__(self):
        self.contain = [[] for x in range(1000)]

    def put(self, key: int, value: int) -> None:
        index = key%1000
        on = True
        for i, x in enumerate(self.contain[index]):
            if x[0] == key:
                self.contain[index][i] = (key, value)
                on = False
                break
        if on:
            self.contain[index].append((key, value))

    def get(self, key: int) -> int:
        index = key%1000
        for i in self.contain[index]:
            if i[0] == key:
                return i[1]
        return -1

    def remove(self, key: int) -> None:
        index = key%1000
        for x, i in enumerate(self.contain[index]):
            if i[0] == key:
                del self.contain[index][x]

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
