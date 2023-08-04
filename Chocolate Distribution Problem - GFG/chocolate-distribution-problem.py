#User function Template for python3

class Solution:

    def findMinDiff(self, A,N,M):
        A.sort()
        res = float("inf")
        for i in range(M-1, len(A)):
            res = min(res, A[i]-A[i-(M-1)])
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
# } Driver Code Ends