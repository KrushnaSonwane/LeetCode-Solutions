# Definition for BigArray.
# class BigArray:
#     def at(self, index: long) -> int:
#         pass
#     def size(self) -> long:
#         pass
class Solution(object):
    def countBlocks(self, nums: Optional['BigArray']) -> int:
        res, n = 0, nums.size()
        i = 0
        while i < n:
            l, r = i, n-1
            while r >= l:
                mid = (r+l) // 2
                if nums.at(mid) == nums.at(i):
                    i, l = mid, mid + 1
                else:
                    r = mid - 1
            res, i = res + 1, i + 1
        return res