class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        if len(derived) == 1 and derived[0] == 0:
            return True
        elif len(derived) == 1:
            return False
        
        # [1, 1, 0] -> [0, 1, 0] or [1, 0, 1]

        # 0, 0, 1
        # 0, 1, 0

        # even and odd

        # 1, 0, 0

        # 1, 0, 0, 0

        # 1, 1, 0, 0, 1, 0

        # 0, 1, 0, 0, 0, 1

        p1, p2 = None, None
        first = None
        for i in range(len(derived)):
            if p1 is None and p2 is None:
                if derived[i] == 0:
                    p1, p2 = 1, 1
                else:
                    p1, p2 = 0, 1
                if not first:
                    first = p1
            elif p2 is None:
                if derived[i] == 0:
                    p2 = p1
                else:
                    p2 = 1 if p1 == 0 else 0
            p1 = p2
            p2 = None
        
    
        return p1 == first

        # 0, 0, 1, 0



        