class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        count = 0
        for i in range(len(colors)):
            if i + 1 >= len(colors):
                color1 = colors[0]
                color2 = colors[1]
            elif i + 2 >= len(colors):
                color1 = colors[i + 1]
                color2 = colors[0]
            else:
                color1 = colors[i + 1]
                color2 = colors[i + 2]

            if colors[i] == 0 and color1 and color2 == 0:
                count += 1
            if colors[i] and color1 == 0 and color2:
                count += 1

        return count
            
