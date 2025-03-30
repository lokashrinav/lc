class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        subsequence_count = 0
        i = 0  # Pointer for target
        
        while i < len(target):
            j = 0  # Pointer for source for each subsequence
            previous_i = i  # To check if we make progress in this pass
            subsequence_count += 1  # We are starting a new subsequence
            
            while j < len(source) and i < len(target):
                if source[j] == target[i]:
                    i += 1
                j += 1
            
            # If no progress is made in one full pass, then it's impossible to form target
            if previous_i == i:
                return -1
            
        return subsequence_count