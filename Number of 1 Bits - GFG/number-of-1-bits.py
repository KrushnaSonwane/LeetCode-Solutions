#User function Template for python3
class Solution:
	def setBits(self, N):
		res = 0
		while N:
		    res += N & 1
		    N >>= 1
		return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.setBits(N)
		print(ans)




# } Driver Code Ends