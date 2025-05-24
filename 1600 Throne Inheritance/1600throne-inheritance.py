class Node:

    def __init__(self, name, parent):
        self.name = name
        self.children = deque()
        self.parent = None
        

class ThroneInheritance:

    def __init__(self, kingName: str):
        self.head = Node(kingName, None)
        self.hset = set([kingName])
        self.hmap = {kingName: self.head}
        self.order = [kingName]
        
    def birth(self, parentName: str, childName: str) -> None:
        node = Node(childName, parentName)
        parent = self.hmap[parentName]
        parent.children.append(node)
        self.hmap[childName] = node
        self.hset.add(childName)
                
    def death(self, name: str) -> None:
        node = self.hmap[name]
        if node.parent:
            parent = self.hmap[node.parent]
            self.hset.remove(name)
        else:
            self.hset.remove(name)
        
    def getInheritanceOrder(self) -> List[str]:
        res = []
        def dfs(node):
            if node.name in self.hset:
                res.append(node.name)

            for child in node.children:
                dfs(child)

        dfs(self.head)

        return res

        

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()