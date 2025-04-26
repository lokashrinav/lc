class Solution:
    def originalDigits(self, s: str) -> str:
        hmap = Counter(s)

        letters = ["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"]
        words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

        '''
        ["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"]
        [zero, one, two, three, four, five, six, seven, eight, nine]

        '''
        hmap2 = defaultdict(list)
        for letter in letters:
            for i in range(len(words)):
                if words[i].count(letter) > 0:
                    hmap2[letter].append(words[i])
        
        print(hmap2)
        
        hmap = Counter(s)
        arr = [0] * 10
        '''
        1, 7
        '''
        
        arr[8] = hmap["g"]
        arr[4] = hmap["u"]
        arr[2] = hmap["w"]
        arr[6] = hmap["x"]
        arr[0] = hmap["z"]
        arr[5] = hmap["f"] - arr[4]
        arr[3] = hmap["r"] - arr[4] - arr[0]
        arr[9] = hmap["i"] - arr[8] - arr[6] - arr[5] 
        arr[7] = hmap["v"] - arr[5]
        arr[1] = hmap["o"] - arr[0] - arr[2] - arr[4]

        str1 = ""
        for i in range(len(arr)):
            str1 += arr[i] * str(i)
        
        return str1

