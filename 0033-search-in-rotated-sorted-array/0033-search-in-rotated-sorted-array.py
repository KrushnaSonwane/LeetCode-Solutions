class Solution:
    def search(self, A: List[int], key: int) -> int:
        if key in A: return A.index(key)
        return -1