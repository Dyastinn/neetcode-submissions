class MyHashSet:

    def __init__(self):
        self.list = []

    def add(self, key: int) -> None:
        if self.contains(key) == True:
            return None
        self.list.append(key) 

    def remove(self, key: int) -> None:
        if self.contains(key) == False:
            return None
        self.list.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.list:
            return True
        return False
        
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)