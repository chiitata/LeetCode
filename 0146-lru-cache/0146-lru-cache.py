class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = self.prev = None

class LRUCache:
    def __init__(self, capacity):
        self.map = {}
        self.capacity = capacity
        self.leftNode = Node(-1, -1)
        self.rightNode = Node(-1, -1)
        self.leftNode.next = self.rightNode
        self.rightNode.prev = self.leftNode
        
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        rightNode = self.rightNode.prev
        self.rightNode.prev = node
        node.next = self.rightNode
        node.prev = rightNode
        rightNode.next = node

    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map[key]
        self.remove(node)
        self.insert(node)
        return self.map[key].val
        

    def put(self, key, value):
        newnode = Node(key, value)
        if key in self.map:
            node = self.map[key]
            self.remove(node)
        self.insert(newnode)
        self.map[key] = newnode
        if len(self.map) > self.capacity:
            del self.map[self.leftNode.next.key]
            self.remove(self.leftNode.next)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)