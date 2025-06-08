class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0

        def multiply(A, B):
            return [
                [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
                [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]
            ]

        def matrix_pow(mat, power):
            # Identity matrix
            result = [[1, 0], [0, 1]]
            while power > 0:
                if power % 2 == 1:
                    result = multiply(result, mat)
                mat = multiply(mat, mat)
                power //= 2
            return result

        base = [[1, 1], [1, 0]]
        res = matrix_pow(base, n - 1)
        return res[0][0]
