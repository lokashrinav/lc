class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = {}
        rst = []
        value = 0
        dict_map = {"A":0,"G":1,"C":2, "T":3}
        for i in range(len(s)):
            if i < 9:
                value = 4 * value + dict_map[s[i]]
            elif i == 9:
                value = 4 * value + dict_map[s[i]]
                res[value] = s[:10]
            else:
                value = (value - dict_map[s[i-10]]*(4**9)) * 4 + dict_map[s[i]]
                if value in res:
                    rst.append(res[value])
                else:
                    res[value] = s[i-9:i+1]
        return list(set(rst))