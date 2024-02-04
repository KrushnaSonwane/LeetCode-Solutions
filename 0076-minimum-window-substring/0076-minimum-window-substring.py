class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if s == t: return s
        if len(t) > len(s): return ''
        tSet, sSet = {}, {}
        count = 0
        for ch in t:
            if ch not in tSet:
                tSet[ch] = 1
                count += 1
            else:
                tSet[ch] += 1
        curr, min_, l, r = 0, len(s), 0, len(s) - 1
        ptr = 0
        flag = False
        for i, ch in enumerate(s):
            if ch in tSet:
                if ch not in sSet:
                    sSet[ch] = 1
                else:
                    sSet[ch] += 1
                
                if sSet[ch] == tSet[ch]:
                    curr += 1
            while curr >= count:
                if min_ >= (i - ptr) + 1:
                    min_ = (i - ptr) + 1
                    l, r = ptr, i
                    print("yes")
                    flag = True
                if s[ptr] in sSet:
                    sSet[s[ptr]] -= 1
                    if sSet[s[ptr]] < tSet[s[ptr]]: 
                        curr -= 1

                ptr += 1

        return s[l : r + 1] if flag else ''