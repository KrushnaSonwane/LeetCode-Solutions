class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        i, j, k = 0, 0, 0
        res = 0
        while len(s1) > i and len(s2) > j and len(s3) > k:
            if s1[i] == s2[j] == s3[k]:
                res += 1
            else:
                break
            i, j, k = i+1, j+1, k+1
        if res == 0: return -1
        return (len(s1)-i) + (len(s2)-j) + (len(s3)-k)