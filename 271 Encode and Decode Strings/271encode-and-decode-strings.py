class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        final = ""
        for str1 in strs:
            final += str(len(str1)) + '-' + str1
        return final
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """

        i = 0
        res = []
        while i < len(s):
            num = 0
            while i < len(s) and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1

            i += 1
            new_str = ""
            saved = i + num
            while i < saved:
                new_str += s[i]
                i += 1
            
            res.append(new_str)

        return res
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))