#User function Template for python3

class Solution:
    def smallestpositive(self, arr, n): 
        # Your code goes here  
        mis=1

        

        arr.sort()

        

        for i in range(n):

            if mis<arr[i]:

                return mis

            else:

                mis+=arr[i]

        

        return mis

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        array = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.smallestpositive(array,n))


# } Driver Code Ends