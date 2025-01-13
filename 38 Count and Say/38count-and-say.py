class Solution:
    def countAndSay(self, n: int) -> str:

        def rle(str1):
            new_str = ""
            count = 0
            prev_str = None
            for i in range(len(str1)):
                if i == 0:
                    count = 1
                    prev_str = str1[i]
                else:
                    if str1[i] == prev_str:
                        count += 1
                    else:
                        new_str += str(count) + prev_str
                        count = 1
                        prev_str = str1[i]
            
            new_str += str(count) + prev_str

            return new_str


        curr = None
        for i in range(n):
            if i == 0:
                curr = "1"
            else:
                curr = rle(curr)
        
        return curr