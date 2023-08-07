#User function Template for python3
class Solution:
	def minDifference(self, arr, n):
		dp = {}
		def dfs(i, sum_):
		    if (i, sum_) not in dp:
    		    if i == n: return abs(sum_)
    		    dp[(i,sum_)] = min(dfs(i+1, sum_+arr[i]), dfs(i+1, sum_-arr[i]))
		    return dp[(i,sum_)]
		return dfs(0, 0)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minDifference(arr, N)
		print(ans)

# } Driver Code Ends