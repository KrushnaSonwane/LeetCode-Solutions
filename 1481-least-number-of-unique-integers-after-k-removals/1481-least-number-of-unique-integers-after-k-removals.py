class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        A = Counter(arr)
        A = sorted([A[num] for num in A])
        while A and k >= A[0]:
            k -= A.pop(0)
        return len(A)