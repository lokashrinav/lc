class Solution:
    def maximumTime(self, time: str) -> str:

        res = list(time)

        if time[0] == "?" and (time[1] == "?" or time[1] in '0123'):
            res[0] = "2"
        elif time[0] == "?":
            res[0] = "1"
        
        if time[1] == "?" and (time[0] == "2" or res[0] == "2"):
            res[1] = "3"
        elif time[1] == "?":
            res[1] = "9"
        
        if time[3] == "?":
            res[3] = "5"
        
        if time[4] == "?":
            res[4] = "9"

        return ''.join(res)
         