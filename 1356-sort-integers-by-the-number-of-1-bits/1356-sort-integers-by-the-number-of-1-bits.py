class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        A = []
        for num in arr:
            res, curr = 0, num
            while curr:
                res += curr % 2
                curr //= 2
            A.append([res, num])
        A.sort()
        return [num for _, num in A]