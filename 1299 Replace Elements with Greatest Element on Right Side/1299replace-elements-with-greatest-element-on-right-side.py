class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        great = None
        for i in range(len(arr) - 1, -1, -1):
            if great is None:
                great = arr[i]
                arr[i] = -1
            else:
                saved = max(arr[i], great)
                arr[i] = great
                great = saved
                
        return arr
            
        