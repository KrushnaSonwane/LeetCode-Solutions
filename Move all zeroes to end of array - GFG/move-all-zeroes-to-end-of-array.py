#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr, n):
    	n=len(arr)
        pointer=0
        zero=0
        for i in range(n):
            if arr[i]!=0:
                arr[pointer]=arr[i]
                pointer+=1
            else:
                zero+=1
        while zero>0:
            arr[pointer]=0
            pointer+=1
            zero-=1
        return arr

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends