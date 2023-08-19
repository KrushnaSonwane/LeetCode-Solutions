#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s):
        hashT = {0:0}
        sum_ = 0
        for i, num in enumerate(arr):
            sum_ += num
            if sum_-s in hashT: return [hashT[sum_-s]+1, i+1]
            hashT[sum_] = i+1
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