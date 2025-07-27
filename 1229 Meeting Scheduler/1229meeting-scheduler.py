class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        
        i = j = 0
        slots1.sort()
        slots2.sort()

        while i < len(slots1) and j < len(slots2):
            start1, end1 = slots1[i]
            start2, end2 = slots2[j]

            start = max(start1, start2)
            end = min(end1, end2)

            if end > start and end - start >= duration:
                return [start, start + duration]
            
            if end1 < end2:
                i += 1
            else:
                j += 1

        return []