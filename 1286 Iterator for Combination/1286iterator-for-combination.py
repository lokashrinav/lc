class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.combs = []
        self._backtrack(characters, combinationLength, 0, [])
        self.index = 0

    def _backtrack(self, chars, k, start, path):
        if len(path) == k:
            self.combs.append(''.join(path))
            return
        # pick each char in lex order
        for i in range(start, len(chars)):
            path.append(chars[i])
            self._backtrack(chars, k, i+1, path)
            path.pop()

    def next(self) -> str:
        result = self.combs[self.index]
        self.index += 1
        return result

    def hasNext(self) -> bool:
        return self.index < len(self.combs)
