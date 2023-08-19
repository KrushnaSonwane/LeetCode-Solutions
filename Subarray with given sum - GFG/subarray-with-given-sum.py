#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s):
        l, r = 0, 0
        if s == 0: return [-1]
        sum_ = 0
        while n > r:
            sum_ += arr[r]
            while sum_ > s:
                sum_ -= arr[l]
                l += 1
            if sum_ == s: 
                return [l+1, r+1]
            r += 1
        return [-1]
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends