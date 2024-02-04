class Solution:
    def resultGrid(self, nums: List[List[int]], threshold: int) -> List[List[int]]:
        A = [[[0, 0] for _ in range(len(nums[0]))] for _ in range(len(nums))]
        for i in range(len(nums)-2):
            for j in range(len(nums[i])-2):
                t = []
                for k in range(i, i+3):
                    a = []
                    for l in range(j, j+3):
                        a.append(nums[k][l])
                    t.append(a)
                flag = False
                for k in range(3):
                    for l in range(3):
                        for x, y in [(k+1, l), (k-1, l), (k, l+1), (k, l-1)]:
                            if 0 <= x < 3 and 0 <= y < 3:
                                if abs(t[k][l] - t[x][y]) <= threshold:
                                    continue
                                flag = True
                if not flag:
                    sum_ = sum(sum(li) for li in t)
                    sum_ //= 9
                    for k in range(i, i+3):
                        for l in range(j, j+3):
                            A[k][l][0] += sum_
                            A[k][l][1] += 1
        res = []
        for i, li in enumerate(A):
            t = []
            for j, (sum_, size) in enumerate(li):
                if size == 0:
                    t.append(nums[i][j])
                else:
                    t.append(sum_ // size)
            res.append(t)
        return res