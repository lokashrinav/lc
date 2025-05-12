class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # 1. reflect into first quadrant and keep x ≥ y ≥ 0
        x, y = abs(x), abs(y)
        if y > x:
            x, y = y, x

        # 2. four tiny squares the linear-combination trick under-counts
        if (x, y) == (0, 0):   return 0
        if (x, y) == (1, 0):   return 3        # also covers (0,1)
        if (x, y) == (1, 1):   return 2
        if (x, y) == (2, 2):   return 4

        # 3. try 0, 1 or 2 EXTRA knight jumps t to land in the 0-mod-3 lattice
        #    and to make both coefficients a, b non-negative.
        #    (Two extras are always enough; proof:  2×(2,1)+(1,2) forms a basis.)
        moves = [( 2, 1), ( 1, 2), (-2, 1), (-1, 2),
                 ( 2,-1), ( 1,-2), (-2,-1), (-1,-2)]

        best = float("inf")

        # helper: compute a, b and returned moves when x+y ≡ 0 (mod 3)
        def combo_cost(x0, y0):
            a = (2*x0 - y0) // 3
            b = (2*y0 - x0) // 3
            if (2*x0 - y0) % 3 or (2*y0 - x0) % 3:
                return None          # not in the lattice
            if a < 0 or b < 0:
                return None          # would need backward bricks
            return a + b             # each brick counts as one move

        # ── 0 extra moves ────────────────────────────────────────────────
        cost = combo_cost(x, y)
        if cost is not None:
            best = min(best, cost)

        # ── 1 extra move ────────────────────────────────────────────────
        for dx1, dy1 in moves:
            cost = combo_cost(x - dx1, y - dy1)
            if cost is not None:
                best = min(best, 1 + cost)

        # ── 2 extra moves (64 possibilities) ────────────────────────────
        for dx1, dy1 in moves:
            x1, y1 = x - dx1, y - dy1
            for dx2, dy2 in moves:
                cost = combo_cost(x1 - dx2, y1 - dy2)
                if cost is not None:
                    best = min(best, 2 + cost)

        # best is now the minimal number of moves
        return best
