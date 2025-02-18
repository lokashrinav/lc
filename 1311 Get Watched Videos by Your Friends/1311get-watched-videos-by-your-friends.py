class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        queue = deque([id])
        visited = set()
        visited.add(id)
        while level:
            for i in range(len(queue)):
                out = queue.popleft()
                for elem in friends[out]:
                    if elem not in visited:
                        visited.add(elem)
                        queue.append(elem)

            level -= 1
                
        hmap = defaultdict(int)
        while queue:
            out = queue.popleft()
            for elem in watchedVideos[out]:
                hmap[elem] += 1
        
        final = sorted(hmap.items(), key=lambda x: (x[1], x[0]))

        return [item[0] for item in final]
        

        


        

        




        