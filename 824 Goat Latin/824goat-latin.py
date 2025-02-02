class Solution:
    def toGoatLatin(self, sentence: str) -> str:

        words = sentence.split(" ")

        new_str = []

        
        for i in range(len(words)):
            queue = deque()
            for char in words[i]:
                queue.append(char)
            if words[i][0] not in 'aeiouAEIOU':
                x = queue.popleft()
                queue.append(x)
            queue.append('ma')
            queue.append('a' * (i + 1))
            
            new_str.append(''.join(list(queue)))

        return ' '.join(new_str)
            

