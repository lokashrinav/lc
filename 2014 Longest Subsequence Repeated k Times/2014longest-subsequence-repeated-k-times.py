from collections import Counter, deque

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        count = Counter(s)
        pool = [c for c in count if count[c] >= k]
        pool.sort(reverse=True)

        def isValid(seq):
            target = seq * k
            i = 0
            for ch in s:
                if ch == target[i]:
                    i += 1
                    if i == len(target):
                        return True
            return False

        queue = deque([''])
        result = ''
        
        while queue:
            curr = queue.popleft()
            for c in pool:
                next_seq = curr + c
                if isValid(next_seq):
                    queue.append(next_seq)
                    if len(next_seq) > len(result) or (len(next_seq) == len(result) and next_seq > result):
                        result = next_seq
        return result
        