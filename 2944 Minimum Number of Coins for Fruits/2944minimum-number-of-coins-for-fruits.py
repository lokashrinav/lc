class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        ans = 0
        free = deque()
        free.append([0, 0])
        
        for i in range(len(prices)):
            ans = free[0][0] + prices[i]
            if free and free[0][1] == i:
                free.popleft()
            while free and free[-1][0] > ans:
                free.pop()
            free.append([ans,2*(i+1)])
        
        return free[0][0]