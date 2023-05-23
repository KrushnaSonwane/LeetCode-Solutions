from sortedcontainers import SortedList
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.arr = SortedList()
        for num in nums:
            self.arr.add(num)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.arr.add(val)
        return self.arr[-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)