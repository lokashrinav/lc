class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        '''
        a, b, c, d
        1, 1, 1
        3, 4
        '''

        diff = [original[i] - original[0] for i in range(len(original))]
        
        bound = None
        for i, (y, x) in enumerate(bounds):
            # Adjust the bounds for copy[0] using the offset at index i.
            current_low = y - diff[i]
            current_high = x - diff[i]
            if bound is None:
                bound = [current_low, current_high]
            else:
                bound[0] = max(bound[0], current_low)
                bound[1] = min(bound[1], current_high)
                if bound[0] > bound[1]:
                    return 0
            # Uncomment the next line to debug the intermediate bounds
            # print(bound)
            
        return bound[1] - bound[0] + 1