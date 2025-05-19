class Solution:
    def average(self, salary: List[int]) -> float:
        
        minNum = min(salary)
        maxNum = max(salary)

        total = sum(salary) - maxNum - minNum

        return total / ((len(salary)) - 2)