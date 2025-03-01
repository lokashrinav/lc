class Solution:
    def minSwaps(self, data: List[int]) -> int:
        one_count = data.count(1)
        count = 0
        final_ind = 0
        for i in range(one_count):
            if data[i] == 1:
                count += 1
            final_ind = i + 1

        maxOnes = count

        for i in range(final_ind, len(data)):
            if data[i] == 1:
                count += 1
            if data[i - final_ind] == 1:
                count -= 1
            maxOnes = max(count, maxOnes)
        
        return one_count - maxOnes
            
            
            
            

        