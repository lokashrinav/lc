class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:

        def isPrime(num):
            if num == 1:
                return False
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    return False
            return True
        
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] >= nums[i]:
                count = nums[i - 1]
                diff = nums[i - 1] - nums[i]
                smth = diff + 1
                changed = None
                while smth < count:
                    if isPrime(smth):
                        changed = smth
                        break
                    smth += 1
                if not changed:
                    return False
                nums[i - 1] -= changed
                print(smth, count, nums)
        
        return True
        

