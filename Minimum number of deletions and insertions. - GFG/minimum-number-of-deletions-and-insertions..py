#User function Template for python3
class Solution:
	def minOperations(self, s1, s2):
	    m, n = len(s1), len(s2)
	    dp = [[-1]*n for _ in range(m)]
	    def dfs(i, j):
	        if i == m: return n - j
	        if j == n: return m - i
	        if dp[i][j]!= -1: return dp[i][j]
	        if s1[i] == s2[j]:
	           res = dfs(i+1, j+1)
	        else:
	           res = min(dfs(i+1, j), dfs(i,j+1)) + 1
            dp[i][j] = res
            return res
        return dfs(0,0)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s1,s2 = input().split()
		ob = Solution()
		ans = ob.minOperations(s1,s2)
		print(ans)
# } Driver Code Ends