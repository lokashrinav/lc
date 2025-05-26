class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        
        hour = 0
        hours = [1, 2, 4, 8]

        minute = 0
        minutes = [1, 2, 4, 8, 16, 32]

        res = set()
        
        def dfs(turnedOn, ind1, ind2):
            nonlocal hour, minute
            print(turnedOn, res)
            if turnedOn == 0:
                str_hour = str(hour)
                str_minute = str(minute)
                if len(str_minute) < 2:
                    str_minute = "0" + str_minute                
                res.add(str_hour + ":" + str_minute)
                return

            for i in range(ind1, len(hours)):
                if hour + hours[i] <= 11:
                    hour += hours[i]
                    dfs(turnedOn - 1, i + 1, ind2)
                    hour -= hours[i]

            for i in range(ind2, len(minutes)):
                if minute + minutes[i] <= 59:
                    minute += minutes[i]
                    dfs(turnedOn - 1, ind1, i + 1)
                    minute -= minutes[i]       

        dfs(turnedOn, 0, 0)
        
        return list(res)

    




        