class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        if label == 1:
            return [1]
        
        path = []
        k = label
        while k > 1:
            path.append(k)

            level = int(math.log2(k)) + 1
            start = 2 ** (level - 1)
            end = 2 ** (level)

            prevStart = 2 ** (level - 2)
            diff = abs(start - 1 - (k // 2))
            new = diff + prevStart
            
            k = new

        path.append(1)

        return path[::-1]