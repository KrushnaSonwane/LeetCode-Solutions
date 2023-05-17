class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = []
        for i in range(numRows):
            if i == 0:
                ans.append([1])
                continue
            if i == 1:
                ans.append([1,1])
                temp = [1,1]
                continue
            temp2 = [1]
            for j in range(1, i):
                temp2.append(temp[j] + temp[j-1])
            else:
                temp2.append(1)
                ans.append(temp2)
                temp = temp2
        return ans