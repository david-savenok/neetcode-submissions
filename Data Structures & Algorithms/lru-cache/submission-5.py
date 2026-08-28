class ListNode:
    def __init__(self, p, n, k, v):
        self.p = p
        self.n = n
        self.k = k
        self.v = v

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.hashmap = {}
        self.head = None
        self.tail = None

    def ins(self, node):
        if node == self.head:
            return node.v
        elif node == self.tail:
            self.tail = node.p
            node.p.n = None
        else:    
            node.p.n = node.n
            node.n.p = node.p
        self.head.p = node
        node.n = self.head
        self.head = node

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            self.ins(node)
            return node.v
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.k = key
            node.v = value
            self.ins(node)
            self.hashmap[key] = node
        else:
            self.size += 1
            node = ListNode(None, self.head, key, value)
            if self.head == None:
                self.head = node
                self.tail = node
                self.hashmap[key] = node
                return

            self.head.p = node
            self.head = node
            self.hashmap[key] = node
            if self.size > self.capacity:
                self.size -= 1
                self.hashmap.pop(self.tail.k)
                self.tail.p.n = None
                self.tail = self.tail.p
