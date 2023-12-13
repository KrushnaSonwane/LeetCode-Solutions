class SegmentTree:
    def createTree(self, A):
        self.tree, n = [0, 0], 1
        self.A = A
        while n <= len(A):
            for _ in range(n):
                self.tree.append(0)
            n *= 2
        for _ in range(n):
            self.tree.append(0)
    def build(self, i, l, r):
        if l == r:
            self.tree[i] = self.A[l-1]
            return
        mid = (r + l) // 2
        self.build(i*2, l, mid)
        self.build(i*2+1, mid+1, r)
        self.tree[i] = self.tree[i*2] + self.tree[i*2+1]
    def up(self, i, l, r, idx, val):
        if l == r:
            diff = val - self.tree[i]
            self.tree[i] = val
            return diff
        mid = (l+r) // 2
        if mid >= idx:
            diff = self.up(i*2, l, mid, idx, val)
        else:
            diff = self.up(i*2+1, mid+1, r,idx, val)
        self.tree[i] += diff
        return diff
    def getSum(self, i, l, r, a, b):
        if b < l:
            return 0
        if a > r:
            return 0
        if a <= l and r <= b:
            return self.tree[i]
        mid = (r+l)//2
        return self.getSum(i*2, l, mid, a, b) + self.getSum(i*2+1, mid+1, r, a, b)

    

class NumArray:

    def __init__(self, nums: List[int]):
        self.obj = SegmentTree()
        self.obj.createTree(nums)
        # print(self.obj.tree)
        self.obj.build(1, 1, len(nums))
        self.nums = nums

    def update(self, index: int, val: int) -> None:
        self.obj.up(1, 1, len(self.nums), index+1, val)        

    def sumRange(self, left: int, right: int) -> int:
        return self.obj.getSum(1, 1, len(self.nums), left+1, right+1)