class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        maxNum = None
        saved = None
        for key, group in groupby(num):
            if len(list(group)) >= 3:
                if maxNum is None:
                    maxNum = int(key * 3)
                    saved = key * 3
                else:
                    if maxNum < int(key * 3):
                        maxNum = int(key * 3)
                        saved = key * 3
        
        return saved if maxNum is not None else ""

        