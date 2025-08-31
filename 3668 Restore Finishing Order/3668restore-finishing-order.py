class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:

        final = []
        friends = set(friends)
        for elem in order:
            if elem in friends:
                final.append(elem)

        return final
        