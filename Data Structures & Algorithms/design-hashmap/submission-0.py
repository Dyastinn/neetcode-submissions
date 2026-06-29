class MyHashMap:

    def __init__(self):
        self.hashMap = [MyLinkList(0,0) for i in range(10**4)]

    def put(self, key: int, value: int) -> None:
        LinkKey = self.hashMap[key % len(self.hashMap)]
        while LinkKey.node:
            if(LinkKey.node.key == key):
                LinkKey.node.value = value
                return
            LinkKey = LinkKey.node
        LinkKey.node = MyLinkList(key, value)

    def get(self, key: int) -> int:
        LinkKey = self.hashMap[key % len(self.hashMap)]
        while LinkKey.node:
            if(LinkKey.node.key == key):
                return LinkKey.node.value
            LinkKey = LinkKey.node
        return -1

    def remove(self, key: int) -> None:
        LinkKey = self.hashMap[key % len(self.hashMap)]
        while LinkKey.node:
            if(LinkKey.node.key == key):
                LinkKey.node = LinkKey.node.node
                return
            LinkKey = LinkKey.node

        
class MyLinkList:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.node = None

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)