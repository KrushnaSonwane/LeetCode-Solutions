class Solution(object):
    def spiralOrder(self, mat):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(mat), len(mat[0])
        l, r, t, b = 0, n - 1, 0, m - 1
        taken, res = 0, []
        while taken < m * n:
            flag = False
            for i in range(l, r + 1, 1):
                res.append(mat[t][i])
                taken += 1
            if m * n <= taken: break
            t += 1
            for i in range(t, b + 1, 1):
                res.append(mat[i][r])
                taken += 1
            if m * n <= taken: break
            r -= 1
            for i in range(r, l - 1, -1):
                res.append(mat[b][i])
                taken += 1
            if m * n <= taken: break
            b -= 1
            for i in range(b, t - 1, -1):
                res.append(mat[i][l])
                taken += 1
            l += 1
        return res