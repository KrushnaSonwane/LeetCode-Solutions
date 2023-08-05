class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        sum_ = sum(nums)
        if (sum_ >= 0 and goal >= 0) or (0 > sum_ and 0 > goal):
            res = abs(abs(sum_)-abs(goal))
        else:
            res = abs(sum_) + abs(goal)
        return res // limit + (1 if res % limit else 0)