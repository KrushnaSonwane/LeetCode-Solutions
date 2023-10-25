#User function Template for python3

class Solution:
    def knapSack(self, n, W, val, wt):
        t = [[-1 for _ in range(W+1)]for _ in range(n+1)]
        for i in range(n+1):
            for j in range(W+1):
                if i==0 or j==0:
                    t[i][j] = 0
                elif wt[i-1] <= j:
                    t[i][j] = max(val[i-1]+t[i][j-wt[i-1]],t[i-1][j])
                else:
                    t[i][j] = t[i-1][j]
        return t[n][W]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, W = [int(x) for x in input().split()]
        val = input().split()
        for itr in range(N):
            val[itr] = int(val[itr])
        wt = input().split()
        for it in range(N):
            wt[it] = int(wt[it])
        
        ob = Solution()
        print(ob.knapSack(N, W, val, wt))
# } Driver Code Ends