class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                res.append([arr[i] / float(arr[j]), arr[i], arr[j]])
        res.sort()
        return [res[k - 1][1], res[k - 1][2]]