class Solution:
    def searchRange(self, A: List[int], key: int) -> List[int]:
        if key not in A: return [-1, -1]
        return [bisect.bisect_left(A, key), bisect_right(A, key)-1]