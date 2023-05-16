class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.hashT = defaultdict(list)
        for i, num in enumerate(nums):
            self.hashT[num].append(i)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        i = random.randint(0, len(self.hashT[target]) - 1)
        return self.hashT[target][i]

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)