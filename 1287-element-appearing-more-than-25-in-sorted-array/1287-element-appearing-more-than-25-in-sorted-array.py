class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        A = Counter(arr)
        for num in A:
            if A[num] > len(arr) / 4: return num
        return -1