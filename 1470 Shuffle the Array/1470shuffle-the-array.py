class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        M = 10000  # A large enough number to store two values at one index

    # Step 1: Encode the second half into the first half
        for i in range(n):
            nums[i] += (nums[i + n] % M) * M

    # Step 2: Decode and rearrange in-place
        j = 2 * n - 1
        for i in range(n - 1, -1, -1):
            y = nums[i] // M
            x = nums[i] % M
            nums[j] = y
            nums[j - 1] = x
            j -= 2

        return nums

# Example usag