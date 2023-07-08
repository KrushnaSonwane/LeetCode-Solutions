class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        res = set()
        count = collections.Counter(tiles)
        def dfs(s, count):
            res.add(s)
            if len(s) == len(tiles): return
            for ch in tiles:
                if count[ch]:
                    count[ch] -= 1
                    dfs(s+ch, count.copy())
                    count[ch] += 1
        dfs('', count)
        return len(res) - 1