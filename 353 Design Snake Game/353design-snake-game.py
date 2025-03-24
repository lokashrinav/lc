class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.w, self.h = width, height
        self.x = self.y = 0
        self.score = 0
        self.queue = deque()
        self.queueSet = set()
        self.foodInd = 0
        self.food = food

    def move(self, direction: str) -> int:
        if direction == 'R':
            self.x += 1
        elif direction == 'L':
            self.x -= 1
        elif direction == 'U':
            self.y -= 1
        else:
            self.y += 1
        
        print(self.queue, self.x, self.y, self.score)
        if not (self.x >= 0 and self.x < self.w and self.y >= 0 and self.y < self.h):
            return -1
        
        if (self.x, self.y) in self.queueSet:
            return -1
        
        if self.foodInd < len(self.food):
            foodY, foodX = self.food[self.foodInd]

            if self.x == foodX and self.y == foodY:
                self.score += 1
                self.queue.append((self.x, self.y))
                self.queueSet.add((self.x, self.y))
                self.foodInd += 1
            else:
                if len(self.queue):
                    out = self.queue.popleft()
                    self.queueSet.remove(out)

                if self.score:
                    self.queue.append((self.x, self.y))
                    self.queueSet.add((self.x, self.y))
        else:
            if len(self.queue):
                out = self.queue.popleft()
                self.queueSet.remove(out)

            if self.score:
                self.queue.append((self.x, self.y))
                self.queueSet.add((self.x, self.y))
                
        return self.score

        

        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)