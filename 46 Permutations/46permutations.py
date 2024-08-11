class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        final = []

        def helper(arr, space):
            if len(space) == 0:
                final.append(arr.copy())
                return

            for i in space:
                arr.append(i)
                x = space.copy()
                x.remove(i)
                helper(arr, x)
                removed = arr.pop()
                x.add(removed)

        helper([], set(nums))
        return final
        