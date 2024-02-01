from sortedcontainers import SortedList
class Solution:
    def minMeetingRooms(self, nums: List[List[int]]) -> int:
        nums.sort()
        A = SortedList([1,1])
        A.discard(1)
        for a, b in nums:
            l, r = 0, len(A)-1
            res = -1
            while r >= l:
                mid = (r + l) // 2
                if A[mid] > a:
                    r = mid - 1
                else:
                    res = mid
                    l = mid + 1
            if res != -1:
                A.discard(A[res])
            A.add(b)
        return len(A)