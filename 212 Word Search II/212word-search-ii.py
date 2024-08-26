class node():
    def __init__(self, val):
        self.end = False
        self.val = val
        self.children = {}

class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]: 
        dummy = head = start = node(0)
        for elem in words:
            dummy = head
            for i in range(len(elem)):
                if elem[i] in dummy.children:
                    saved = dummy.children[elem[i]]
                else:                
                    saved = node(elem[i])
                dummy.children[elem[i]] = saved
                dummy = saved
                if i == len(elem) - 1:
                    dummy.end = True
        
        res = set()

        def check(head, node, string):
            y, x = node
            if node in visited or not (x >= 0 and y >= 0 and x < len(board[0]) and y < len(board)):
                return
            visited.add(node)
            letter = board[y][x]
            string += letter
            if letter in head.children and head.children[letter].end == True:
                res.add(string)
            if letter in head.children:
                elem = head.children[letter]
                check(elem, (y + 1, x), string)
                check(elem, (y - 1, x), string)
                check(elem, (y, x + 1), string)
                check(elem, (y, x - 1), string)
            visited.remove(node)
            return

            
        for y in range(len(board)):
            for x in range(len(board[0])):
                visited = set()
                head = start
                check(head, (y, x), "")
        
        return list(res)
        