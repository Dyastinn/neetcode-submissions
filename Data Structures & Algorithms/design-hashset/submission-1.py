class MyHashSet:

    def __init__(self):
        self.set = [LinkList(0) for i in range(10**4)]

    def add(self, key: int) -> None:
        LinkKey = self.set[key % len(self.set)]   
        while LinkKey.node:
            if(LinkKey.node.key == key):
                return
            LinkKey = LinkKey.node    
        LinkKey.node = LinkList(key)

    def remove(self, key: int) -> None:
        LinkKey = self.set[key % len(self.set)]   
        while LinkKey.node:
            if(LinkKey.node.key == key):
                LinkKey.node = LinkKey.node.node
                return
            LinkKey = LinkKey.node    

    def contains(self, key: int) -> bool:
        LinkKey = self.set[key % len(self.set)]
        while LinkKey.node:
            if(LinkKey.node.key == key):
                return True
            LinkKey = LinkKey.node
        return False
        
class LinkList:
    def __init__(self, key: int):
        self.key = key
        self.node = None
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)