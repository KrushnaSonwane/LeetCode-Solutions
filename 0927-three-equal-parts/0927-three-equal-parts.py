class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        limit = arr.count(1)
        if limit == 0: return [0, 2]
        if limit % 3: return [-1, -1]
        limit //= 3
        i, count = len(arr)-1, 0

        def solve(i):
            A, count = [], 0
            while count != limit:
                A.append(arr[i])
                count += arr[i] == 1
                i  -= 1
            return A[::-1], i

        A, i = solve(i)
        B, i = solve(i)
        C, i = solve(i)
        n = len(A)

        while A and B and C:
            if A[0] == B[0] == C[0]:
                A.pop(0)
                B.pop(0)
                C.pop(0)
            else: return [-1, -1]
            
        if A: return [-1, -1]
        return [i+(n-1)+1, len(arr)-(n + len(B))]
