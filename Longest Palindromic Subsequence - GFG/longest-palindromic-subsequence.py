#User function Template for python3

class Solution:

    def longestPalinSubseq(self, S):
        dp = [[-1 for _ in S] for _ in S]
        def dfs(i, j):
            if i > j: return 0
            if i == j: return 1
            if dp[i][j] != -1: return dp[i][j]
            res = 0
            if S[i] == S[j]:
                res = 2 + dfs(i+1, j-1)
            else:
                res = max(dfs(i+1, j), dfs(i, j-1))
            dp[i][j] = res
            return res
        return dfs(0,len(S)-1)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        ans = ob.longestPalinSubseq(s)
        print(ans)
# } Driver Code Ends