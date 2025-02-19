class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        answer = []

        back_cache = {}
        curr_cache = {}

        def dfs(num, count):
            if num in back_cache:
                return back_cache[num]

            if num in curr_cache:
                record[0] = num
                return count - curr_cache[num]

            curr_cache[num] = count
            
            returned = dfs(edges[num], count + 1)

            if record[0] is not None:
                curr_cache[num] = returned
            else:
                curr_cache[num] = 1 + returned

            if record[0] == num:
                record[0] = None
            
            return curr_cache[num]
                             

        for i in range(len(edges)):
            record = [None]
            if i not in back_cache:
                dfs(i, 0)
                back_cache.update(curr_cache)
                curr_cache = {}
                answer.append(back_cache[i])
            else:
                answer.append(back_cache[i])
        
        return answer