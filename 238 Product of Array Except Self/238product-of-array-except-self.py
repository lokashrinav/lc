class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        1 a a*b a*b*c a*b*c*d

        a*b*c*d  b*c*d   c*d  d 1

        '''
        prefix = [1]
        postfix = [1]
        for i in range(len(nums)):
            prefix.append(prefix[-1] * nums[i])
            postfix.append(postfix[-1] * nums[-i-1])
        postfix.reverse()

        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * postfix[i + 1])

        return res


