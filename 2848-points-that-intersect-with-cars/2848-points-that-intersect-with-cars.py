class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort()
        visit = set()
        for l, r in nums:
            for i in range(l, r+1):
                visit.add(i)
        return len(visit)