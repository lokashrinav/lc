class Solution:
    def containsPattern(self, arr: list[int], m: int, k: int) -> bool:
        streak = 0                 # current run of “good” pairs
        need   = m * (k - 1)       # how long the run must reach

        # compare each element with the one m steps ahead
        for i in range(len(arr) - m):
            if arr[i] == arr[i + m]:
                streak += 1
                if streak == need:     # found k blocks in a row
                    return True
            else:
                streak = 0             # reset when pair breaks

        return False

