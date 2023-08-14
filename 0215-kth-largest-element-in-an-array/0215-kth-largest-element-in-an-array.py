class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        A = []
        for num in nums:
            if len(A) < k: heappush(A, num)
            elif A[0] < num: heapreplace(A, num)
        return heappop(A)