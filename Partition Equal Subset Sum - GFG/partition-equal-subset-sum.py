# User function Template for Python3

class Solution:
    def equalPartition(self, N, arr):
        # code here
        sum_, dp = sum(arr), {}
        if sum_ % 2: return 0
        def dfs(i, sum_):
            if i == N:
                return sum_ == 0
            if (i, sum_) in dp: return dp[(i, sum_)]
            res = dfs(i+1, sum_)
            if sum_ >= arr[i]:
                res = res or dfs(i+1, sum_ - arr[i])
            dp[(i, sum_)] = res
            return res
        return dfs(0, sum_//2)

#{ 
 # Driver Code Starts
# Initial Template for Python3

import sys
input = sys.stdin.readline
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])
        
        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")
# } Driver Code Ends