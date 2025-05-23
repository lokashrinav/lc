class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:

        '''
        dsu
        '''

        '''

        num_remove, total_sum, num_children

        '''

        paths = defaultdict(list)

        for i in range(1, len(parent)):
            paths[parent[i]].append(i)
        
        def dfs(num):
            
            total_sum = value[num]
            total_child = 0
            remove_total = 0

            for elem in paths[num]:
                remove, sum1, child = dfs(elem)
                total_sum += sum1
                remove_total += remove
                total_child += child
            
            if 0 == total_sum:
                return (total_child + 1, total_sum, total_child + 1)
            else:
                return (remove_total, total_sum, total_child + 1)

        return nodes - dfs(0)[0]



        