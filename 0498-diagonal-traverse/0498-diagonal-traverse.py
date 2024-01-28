class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        hashT = defaultdict(list)
        max_ = 0
        for i in range(len(mat)):
            size = i
            for num in mat[i]:
                hashT[size].append(num)
                size += 1
                max_ = max(max_, size)
        res = []
        for i in range(size):
            A = hashT[i]
            if i % 2 == 0: A.reverse()
            res += A
        return res