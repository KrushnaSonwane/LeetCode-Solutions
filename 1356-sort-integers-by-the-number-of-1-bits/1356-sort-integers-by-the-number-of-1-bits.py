class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        A = []
        for num in arr:
            A.append([bin(num).count('1'), num])
        A.sort()
        return [num for _, num in A]