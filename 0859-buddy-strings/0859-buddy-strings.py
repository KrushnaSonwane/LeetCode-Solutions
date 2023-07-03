class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return 0
        A = collections.Counter(s)
        B = collections.Counter(goal)
        flag = False
        for ch in A:
            if ch not in B or A[ch] != B[ch]: return 0
            if B[ch] >= 2: flag = True
        count = 0
        for a, b in zip(s, goal):
            if a != b: count += 1
        if count == 0 and flag: return 1
        if count == 2: return 1
        return 0