class Solution:
    def badSensor(self, sensor1: List[int], sensor2: List[int]) -> int:

        def check(p, i):
            count = 0
            while p < len(sensor1)  and i < len(sensor2) and sensor1[p] == sensor2[i]:
                p += 1
                i += 1
            
            return p == len(sensor1) or i == len(sensor2)

        for i in range(len(sensor1)):
            if sensor1[i] != sensor2[i]:
                if i >= len(sensor1) - 1:
                    return -1

                if check(i + 1, i):
                    if check(i, i + 1):
                        print("a")
                        return -1
                    return 2
                else:
                    if check(i, i + 1):
                        return 1
                    return -1        
        return -1
        