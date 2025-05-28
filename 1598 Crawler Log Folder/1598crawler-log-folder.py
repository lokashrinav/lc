class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        s = 0

        for elem in logs:
            if elem == "./":
                continue
            if elem == "../":
                s = max(0, s - 1)
            else:
                s += 1
        
        return s
            