class FileSystem:

    def __init__(self):
        self.hmap = {}

    def createPath(self, path: str, value: int) -> bool:
        if path in self.hmap:
            return False
            
        s = path.split("/")
        s = [elem for elem in s if elem]

        if len(s) == 1:
            self.hmap['/' + s[0]] = value
            return True

        #print(s, '/' + '/'.join(s[:-1]))

        if len(s) == 1 or '/' + '/'.join(s[:-1]) in self.hmap:
            self.hmap['/' + '/'.join(s)] = value
            return True

        return False                

    def get(self, path: str) -> int:
        if path in self.hmap:
            return self.hmap[path]
        else:
            return -1
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)