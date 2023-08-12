#User function Template for python3
import bisect
class Solution:
    
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self,A,n):
        # code here
        stack = []
        for num in A:
            if not stack or stack[-1] < num:
                stack.append(num)
            else:
                i = bisect.bisect_left(stack, num)
                stack[i]=num
        return len(stack)
       



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = [ int(x) for x in input().split() ]
        ob=Solution()
        print(ob.longestSubsequence(a,n))
# } Driver Code Ends