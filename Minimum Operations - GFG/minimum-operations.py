#User function Template for python3

class Solution:
    def minOperation(self, n):
        # code here 
        res=0
        
        while n>0:
            if n%2==1:
                n=n-1
                res=res+1
            else:
                n=n//2
                res=res+1
        
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.minOperation(n))
# } Driver Code Ends