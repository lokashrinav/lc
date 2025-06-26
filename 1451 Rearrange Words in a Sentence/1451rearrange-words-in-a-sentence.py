class Solution:
    def arrangeWords(self, text: str) -> str:

        arr = [[] for _ in range(len(text))]
        res = []

        text = text.split(" ")

        for i in range(len(text)):
            arr[len(text[i]) - 1].append(text[i].lower())
        
        print(arr)

        for i in range(len(arr)):
            for p in range(len(arr[i])):
                res.append(arr[i][p])
        
        print(res)

        res[0] = res[0][0].upper() + res[0][1:]
        
        return ' '.join(res)

        