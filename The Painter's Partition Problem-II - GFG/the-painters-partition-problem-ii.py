#User function Template for python3

class Solution:
    def minTime (self, arr, n, k):
        l, r = min(arr), sum(arr)
        def isValid(m):
            count, sum_ = 0, 0
            for num in arr:
                if num > m: return 0
                if num+sum_ > m:
                    count += 1
                    sum_ = num
                else: sum_ += num
            return count + 1 <= k
        while r > l:
            m = (r+l)//2
            if isValid(m):
                r = m
            else:
                l = m + 1
        return l
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        str = input().split()
        k = int(str[0])
        n = int(str[1])
        arr = input().split()
        for itr in range(n):
            arr[itr] = int(arr[itr])

        ob = Solution()
        print(ob.minTime(arr,n,k))
# } Driver Code Ends