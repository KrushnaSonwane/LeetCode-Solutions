class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        arr = self.nums.copy()
        for i in range(len(self.nums)):
            j = random.randint(0, i)
            arr[i], arr[j] = arr[j], arr[i]
        return arr
            


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()