class Solution(object):
    def largestTimeFromDigits(self, arr):
        """
        :type arr: List[int]
        :rtype: str
        """
        if sum(arr) == 0: return '00:00'
        hh, mm = 0, 0
        for i in range(4):
            for j in range(4):
                if j == i: continue
                for k in range(4):
                    if j == k or k == i: continue
                    for l in range(4):
                        if l in [i, j, k]: continue
                        h, m = arr[i] * 10 + arr[j], arr[k] * 10 + arr[l]
                        if h >= 24 or m >= 60: continue
                        if h > hh:
                            hh, mm = h, m
                        elif h == hh:
                            mm = max(mm, m)
        if not hh and not mm: return ''
        if 10 > hh:
            if 10 > mm: return '0' + str(hh) + ':' + '0' + str(mm)
            return '0' + str(hh) + ':' + str(mm)
        if 10 > mm:
            return str(hh) + ":" + '0' + str(mm)
        return str(hh) + ':' + str(mm)