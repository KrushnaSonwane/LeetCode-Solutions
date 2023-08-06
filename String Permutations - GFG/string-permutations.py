#User function Template for python3

class Solution:
    def permutation(self,s):
        res = []
        A = [ch for ch in s]
        def dfs(i):
            if i == len(s):
                res.append(''.join(A))
                return
            for j in range(i, len(A)):
                A[i], A[j] = A[j], A[i]
                dfs(i+1)
                A[i], A[j] = A[j], A[i]
        dfs(0)
        return sorted(res)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T=int(input())
    while(T>0):
        s=input()
        ob=Solution()
        ans=ob.permutation(s)
        for i in ans:
            print(i,end=" ")
        print()
        
        T-=1
# } Driver Code Ends