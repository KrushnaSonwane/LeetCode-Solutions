#User function Template for python3
import collections
class Solution:

    def longestKSubstr(self, s, k):
        res, hashT = -1, collections.defaultdict(int)
        j = 0
        for i, ch in enumerate(s):
            hashT[ch] += 1
            while len(hashT) > k:
                hashT[s[j]] -= 1
                if hashT[s[j]] == 0:
                    del hashT[s[j]]
                j += 1
            if len(hashT)==k: res = max(res, i - j + 1)
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()
        k = int(input())

        solObj = Solution()

        ans = solObj.longestKSubstr(s, k)

        print(ans)

# } Driver Code Ends