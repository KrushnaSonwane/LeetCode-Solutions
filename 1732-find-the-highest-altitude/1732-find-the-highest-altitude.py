class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        return max(max(0, sum(gain[:i + 1])) for i in range(len(gain)))