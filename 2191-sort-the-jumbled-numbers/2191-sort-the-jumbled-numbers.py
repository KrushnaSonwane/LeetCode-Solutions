class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        queue = []
        for i, num in enumerate(nums):
            num = [ch for ch in str(num)]
            for j, digit in enumerate(num):
                num[j] = str(mapping[int(digit)])
            heapq.heappush(queue, [int(''.join(num)), i])
        return [nums[heapq.heappop(queue)[1]] for _ in range(len(queue))]