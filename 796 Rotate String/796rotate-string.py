class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        if len(goal) != len(s):
            return False
        
        if Counter(s) != Counter(goal):
            return False

        goal += goal

        return s in goal
        