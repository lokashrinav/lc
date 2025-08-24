class Solution:
    def subarraysWithMoreOnesThanZeroes(self, nums: List[int]) -> int:
        mod = int(1e9+7)
        equalOnes,moreOnes = 0,0
        netOnes,ans = 0,0
        # dict for number of times we had netOnes, for array [0...idx]
        cntNetOnes = defaultdict(int)
        cntNetOnes[0] = 1
        for num in nums:
            netOnes = netOnes+1 if num==1 else netOnes-1
            # num==1, all equal ones become moreOnes, plus the single value subarray at current index
            # num==0, all mores ones that had 'netOnes' net ones become equalOnes
            moreOnes = equalOnes+moreOnes+1 if num==1 else moreOnes-cntNetOnes[netOnes]
            equalOnes = cntNetOnes[netOnes]
            cntNetOnes[netOnes]+=1
            ans = (ans+moreOnes)%mod
        return ans