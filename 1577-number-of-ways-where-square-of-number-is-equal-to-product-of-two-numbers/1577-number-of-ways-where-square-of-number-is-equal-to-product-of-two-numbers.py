class Solution:
    def numTriplets(self, A: List[int], B: List[int]) -> int:
        def solve(A, B):
            hashT = defaultdict(int)
            for num in A:
                hashT[num**2]+=1
            res = 0
            for i in range(len(B)):
                for j in range(i+1, len(B)):
                    curr = B[i]*B[j]
                    if curr in hashT: res += hashT[curr]
            return res
        return solve(A, B) + solve(B, A)