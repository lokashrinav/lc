class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        
        new = int(math.floor(purchaseAmount / 10 + 0.5))

        return 100 - new * 10

