class Solution:
    def maximumRequests(self, n: int, A: List[List[int]]) -> int:
        hashT = defaultdict(int)
        def dfs(i, count):
            if i == len(A):
                for val in hashT.values():
                    if val != 0: break
                else: return count
                return 0
            hashT[A[i][0]] += 1
            hashT[A[i][1]] -= 1
            res = dfs(i+1, count + 1)
            hashT[A[i][0]] -= 1
            hashT[A[i][1]] += 1
            res = max(res, dfs(i + 1, count))
            return res
        dfs(0, 0)
        return dfs(0, 0)