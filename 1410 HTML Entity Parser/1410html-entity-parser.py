class Solution:
    def entityParser(self, text: str) -> str:

        p = 0
        res = []

        while p < len(text):
            if text[p:p+6] == "&quot;":
                res.append("\"")
                p = p + 6
            elif text[p:p+6] == "&apos;":
                res.append("\'")
                p = p + 6
            elif text[p:p+5] == "&amp;":
                res.append("&")
                p = p + 5
            elif text[p:p+4] == "&gt;":
                res.append(">")
                p = p + 4
            elif text[p:p+4] == "&lt;":
                res.append("<")
                p = p + 4
            elif text[p:p+7] == "&frasl;":
                res.append("/")
                p = p + 7
            else:
                res.append(text[p])
                p += 1
        
        return ''.join(res)
        