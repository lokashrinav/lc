class Node:
    def __init__(self):
        self.curr = 0
        self.smth = None
        self.end = None
        self.children = {}

class MapSum:

    def __init__(self):
        self.head = Node()       
        self.head.curr = 0 

    def printNode(self, node):
        queue = deque()
        queue.append(node)

        while queue:
            for i in range(len(queue)):
                out = queue.popleft()
                for child in out.children.values():
                    queue.append(child)
                print(out.smth, out.curr, end=' ')
            print("")

    def insert(self, key: str, val: int) -> None:
        node = self.head
        for i in range(len(key)):
            if key[i] in node.children:
                node.children[key[i]].curr += val
                node = node.children[key[i]]
            else:
                newNode = Node()
                newNode.curr = val
                node.children[key[i]] = newNode
                newNode.smth = key[i]
                node = newNode

        curr = node.end
        if curr:
            node = self.head
            for i in range(len(key)):
                node.children[key[i]].curr -= curr
                node = node.children[key[i]]

        node.end = val
            
    def sum(self, prefix: str) -> int:
        node = self.head
        self.printNode(self.head)
        print("Hello")
        for i in range(len(prefix)):
            if prefix[i] not in node.children:
                return 0
            node = node.children[prefix[i]]
        
        return node.curr

        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)