class Solution:
    def longestPalindrome(self, s: str) -> str:

        longest = 1
        saved = s[0]

        for i in range(len(s)):
            l, r = i, i
            curr = 0
            queue = deque()
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if l == r:
                        queue.append(s[l])
                        curr += 1
                    else:
                        queue.appendleft(s[l])
                        queue.append(s[r])
                        curr += 2
                    l -= 1
                    r += 1
                else:
                    break

            if curr > longest:
                longest = max(longest, curr)
                saved = ''.join(queue)

            l, r = i - 1, i
            curr = 0
            queue = deque()
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    curr += 2
                    queue.appendleft(s[l])
                    queue.append(s[r])
                    l -= 1
                    r += 1
                else:
                    break

            if curr > longest:
                longest = max(longest, curr)
                saved = ''.join(queue) 
        
        return saved
            

