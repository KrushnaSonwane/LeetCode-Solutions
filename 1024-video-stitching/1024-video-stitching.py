class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        if clips[0][0] != 0: return -1
        dp = {}
        def dfs(i, l, r):
            if r >= time: return 0
            if i == len(clips):
                if r >= time: return 0
                else: return -1
            if (i, l, r) in dp: return dp[(i, l, r)]
            res = dfs(i + 1, l, r)
            if clips[i][0] > r: return -1
            else:
                if clips[i][0] >= l and clips[i][1] >= l:
                    temp = dfs(i + 1, l, max(r, clips[i][1]))
                    if temp != -1:
                        if res == -1: res = temp + 1
                        else: res = min(res, temp + 1)
            dp[(i, l, r)] = res
            return res
        return dfs(0, 0, 0)