class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:

        prev = 0
        maxNum = 0
        saved = ""

        for i in range(len(releaseTimes)):
            if releaseTimes[i] - prev >= maxNum:
                if maxNum == releaseTimes[i] - prev:
                    saved = max(saved, keysPressed[i])
                else:
                    maxNum = releaseTimes[i] - prev
                    saved = keysPressed[i]
            prev = releaseTimes[i]
        
        return saved
        