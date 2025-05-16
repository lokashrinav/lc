class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        hamming = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                if len(words[i]) == len(words[j]):
                    hamming[i][j] = sum(c1 != c2 for c1, c2 in zip(words[i], words[j]))
                    hamming[j][i] = hamming[i][j]
        dp = [1] * n
        prev = [-1] * n
        for i in range(n):
            for j in range(i):
                if groups[i] != groups[j] and hamming[i][j] == 1 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
        max_length, last_index = max((v, i) for i, v in enumerate(dp))
        sequence = []
        while last_index != -1:
            sequence.append(words[last_index])
            last_index = prev[last_index]
        return sequence[::-1]