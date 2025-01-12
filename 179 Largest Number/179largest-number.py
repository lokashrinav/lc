class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        if 0 in set(nums) and len(set(nums)) == 1:
            return "0"

        def compare(num1, num2):
            str1 = str(num1)
            str2 = str(num2)
            
            first = str1 + str2
            second = str2 + str1

            if first[0] == "0" and second[0] == "0":
                return 0
            elif first[0] == "0":
                return 1
            elif second[0] == "0":
                return -1

            if first > second:
                return -1
            elif first == second:
                return 0
            else:
                return 1

        nums.sort(key=cmp_to_key(compare))

        return ''.join([str(num) for num in nums])
        