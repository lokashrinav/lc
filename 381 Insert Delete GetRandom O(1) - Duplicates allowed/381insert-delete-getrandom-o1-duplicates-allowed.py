class RandomizedCollection:
    def __init__(self):
        self.arr = []                    # stores all elements
        self.indices = defaultdict(set)  # val -> set of indices in arr
    
    def insert(self, val: int) -> bool:
        was_empty = not self.indices[val]
        self.arr.append(val)
        self.indices[val].add(len(self.arr) - 1)
        return was_empty
    
    def remove(self, val: int) -> bool:
        if not self.indices[val]:
            return False
        
        # Get any index where val appears
        remove_idx = self.indices[val].pop()
        last_idx = len(self.arr) - 1
        last_val = self.arr[last_idx]
        
        # Replace element at remove_idx with last element
        self.arr[remove_idx] = last_val
        
        # Update indices for the moved element (if it actually moved)
        if remove_idx != last_idx:
            self.indices[last_val].add(remove_idx)
            self.indices[last_val].discard(last_idx)
        
        self.arr.pop()
        return True
    
    def getRandom(self) -> int:
        return random.choice(self.arr)