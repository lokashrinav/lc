class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:

        lock_stack = []
        unlock_stack = []

        for i in range(len(s)):
            if locked[i] == '0':
                unlock_stack.append(i)
            elif s[i] == '(':
                lock_stack.append(i)
            else:
                if lock_stack:
                    lock_stack.pop()
                elif unlock_stack:
                    unlock_stack.pop()
                else:
                    return False

        while lock_stack and unlock_stack and lock_stack[-1] < unlock_stack[-1]:
            lock_stack.pop()
            unlock_stack.pop()

        if lock_stack or len(unlock_stack) % 2 == 1:
            return False

        return True

        