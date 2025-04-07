class MyCalendar:

    def __init__(self):
        self.arr = []

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.arr:
            self.arr.append([startTime, endTime])
            return True
        else:
            flag = False
            for i in range(len(self.arr)):
                condition1 = (startTime >= self.arr[i][0] and endTime < self.arr[i][0]) or (startTime <= self.arr[i][0] and endTime > self.arr[i][0])
                condition2 = (startTime >= self.arr[i][0] and self.arr[i][1] > startTime) or (self.arr[i][0] >= startTime and endTime > self.arr[i][0])
                if condition1 or condition2:
                    flag = True
            if not flag:
                self.arr.append([startTime, endTime])
            
            return not flag

            
        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)