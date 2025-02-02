class Solution:
    def maximumSwap(self, num: int) -> int:
        idk = list(str(num))
        last_index = {digit: i for i, digit in enumerate(idk)}

        for i in range(len(idk)):
            for digit in range(9, int(idk[i]), -1):
                if str(digit) in last_index and last_index[str(digit)] > i:
                    idk[i], idk[last_index[str(digit)]] = idk[last_index[str(digit)]], idk[i]
                    return int(''.join(idk))
        return int(num)
        