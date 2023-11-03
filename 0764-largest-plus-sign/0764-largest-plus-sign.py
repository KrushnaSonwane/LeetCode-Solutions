class Solution:
    def orderOfLargestPlusSign(self, n: int, A: List[List[int]]) -> int:
        A = {(i, j) for i, j in A}
        up, down = [[0 for _ in range(n)] for _ in range(n)], [[0 for _ in range(n)] for _ in range(n)]
        left, right = [[0 for _ in range(n)] for _ in range(n)], [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            last = 0
            for j in range(n):
                last = last + 1 if (i, j) not in A else 0
                right[i][j] = last

        for i in range(n):
            last = 0
            for j in range(n-1, -1, -1):
                last = last + 1 if (i, j) not in A else 0
                left[i][j] = last

        for i in range(n):
            last = 0
            for j in range(n):
                last = last + 1 if (j, i) not in A else 0
                down[j][i] = last

        for i in range(n-1, -1, -1):
            last = 0
            for j in range(n-1, -1, -1):
                last = last + 1 if (j, i) not in A else 0
                up[j][i] = last

        return max(min(left[i][j], right[i][j], up[i][j], down[i][j]) for j in range(n) for i in range(n))