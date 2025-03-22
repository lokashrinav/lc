class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        chars = [chr(i) for i in range(97, 103)]
        chars += [chr(i) for i in range(65, 71)]

        if queryIP.count('.') == 3:
            i = 0
            while i < len(queryIP):
                if queryIP[-1] == '.':
                    return 'Neither'

                num = 0
                new_str = ""
                while i < len(queryIP) and queryIP[i] != '.':
                    if not queryIP[i].isdigit():
                        return 'Neither'
                    num = num * 10 + int(queryIP[i])
                    new_str += queryIP[i]
                    i += 1
                
                if not new_str:
                    return 'Neither'
                
                if len(new_str) > 1 and new_str[0] == '0':
                    return 'Neither'

                if num < 0 or num > 255:
                    return 'Neither'

                i += 1

            return 'IPv4'

        elif queryIP.count(':') == 7:
            if queryIP[-1] == ':':
                return 'Neither'
            i = 0
            while i < len(queryIP):
                num = 0
                new_str = ""
                while i < len(queryIP) and queryIP[i] != ':':
                    if not (queryIP[i].isdigit() or queryIP[i] in chars):
                        return 'Neither'
                    new_str += queryIP[i]
                    i += 1
                if not new_str:
                    return 'Neither'

                if len(new_str) > 4:
                    return 'Neither'

                i += 1
            
            return 'IPv6'
        else:
            return "Neither"