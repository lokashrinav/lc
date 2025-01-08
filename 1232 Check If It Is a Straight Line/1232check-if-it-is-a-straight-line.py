class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        prev = None
        changed = None
        for i in range(len(coordinates) - 1):
            slope = (coordinates[i + 1][1] - coordinates[i][1]) / (coordinates[i + 1][0] - coordinates[i][0]) if coordinates[i + 1][0] - coordinates[i][0] != 0 else None

            if changed is not None and slope != prev:
                return False
            changed = True
            prev = slope
        return True
        