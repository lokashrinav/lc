from sortedcontainers import SortedSet

class NumberContainers:

    def __init__(self):
        self.indices_to_num = {}
        self.num_to_indices = {}

    def change(self, index: int, number: int) -> None:
        if index in self.indices_to_num:
            old_num = self.indices_to_num[index]
            self.num_to_indices[old_num].discard(index)
            if len(self.num_to_indices[old_num]) == 0:
                del self.num_to_indices[old_num]

        self.indices_to_num[index] = number
        if number not in self.num_to_indices:
            self.num_to_indices[number] = SortedSet()
        self.num_to_indices[number].add(index)

    def find(self, number: int) -> int:
        if self.num_to_indices and number in self.num_to_indices:
            return self.num_to_indices[number][0]
        return -1



# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)