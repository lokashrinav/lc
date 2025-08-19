class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:


        for i in range(1, memory1 + memory2 + 2):
            if i > max(memory1, memory2):
                return [i, memory1, memory2]
            else:
                if memory1 >= memory2:                        
                    memory1 -= i
                else:
                    memory2 -= i
        
        
        
        

                



        