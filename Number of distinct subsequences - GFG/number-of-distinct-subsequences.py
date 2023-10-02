#User function Template for python3

class Solution:
	def distinctSubsequences(self, S):
		# code here
		MOD = 10**9 + 7
        last_occurrence = {}
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i, char in enumerate(s, start=1):
            dp[i] = (2 * dp[i - 1]) % MOD
            if char in last_occurrence:
                dp[i] = (dp[i] - dp[last_occurrence[char]] + MOD) % MOD
            last_occurrence[char] = i - 1
        return dp[-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()

		ob = Solution()
		answer = ob.distinctSubsequences(s)
		print(answer)

# } Driver Code Ends