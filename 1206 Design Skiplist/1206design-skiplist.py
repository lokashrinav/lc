import random

class ListNode:
    def __init__(self, val, level):
        self.val = val
        self.forward = [None] * (level + 1)

class Skiplist:

    def __init__(self):
        self.MAX_LEVEL = 16
        self.head = ListNode(-1, self.MAX_LEVEL)
        self.level_count = 0
    
    def randomLevel(self):
        level = 0
        while random.random() < 0.5 and level < self.MAX_LEVEL:
            level += 1
        return level

    def search(self, target: int) -> bool:
        current = self.head
        for i in range(self.level_count, -1, -1):
            while current.forward[i] and current.forward[i].val < target:
                current = current.forward[i]

        current = current.forward[0]

        return current is not None and current.val == target

    def add(self, num: int) -> None:
        update = [None] * (self.MAX_LEVEL + 1)
        current = self.head

        for i in range(self.level_count, -1, -1):
            while current.forward[i] and current.forward[i].val < num:
                current = current.forward[i]
            update[i] = current
        
        current = current.forward[0]

        new_level = self.randomLevel()
        
        if new_level > self.level_count:
            for i in range(self.level_count + 1, new_level + 1):
                update[i] = self.head
            self.level_count = new_level
        
        newNode = ListNode(num, new_level)

        for i in range(new_level + 1):
            newNode.forward[i] = update[i].forward[i]
            update[i].forward[i] = newNode
            
    def erase(self, num: int) -> bool:
        current = self.head
        update = [None] * (self.MAX_LEVEL + 1)

        for i in range(self.level_count, -1, -1):
            while current.forward[i] and current.forward[i].val < num:
                current = current.forward[i]
            update[i] = current
        
        current = current.forward[0]

        if current and current.val == num:
            for level in range(self.level_count + 1):
                if update[level].forward[level] == current:
                    update[level].forward[level] = current.forward[level]
            
            while self.level_count > 0 and self.head.forward[self.level_count] is None:
                self.level_count -= 1

            return True
        return False
        


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)