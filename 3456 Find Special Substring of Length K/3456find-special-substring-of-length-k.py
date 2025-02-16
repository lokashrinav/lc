class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:

        k -= 1
        for i in range(k, len(s)):
            # print(i - k, i + 1)
            # print(s[i-k:i])
            if len(set(s[i-k:(i+1)])) == 1:
                changed = True
                if i - k != 0 and s[i - k] == s[i - k - 1]:
                    changed = False

                if i < len(s) - 1 and s[i] == s[i + 1]:
                    changed = False

                if changed:
                    return True

        return False
                