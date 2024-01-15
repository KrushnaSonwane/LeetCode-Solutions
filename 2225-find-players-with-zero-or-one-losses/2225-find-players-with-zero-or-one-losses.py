class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lose, win = defaultdict(int), defaultdict(int)
        for a, b in matches:
            lose[b] += 1
            win[a] += 1
        a, b = [], []
        for num in lose:
            if lose[num] == 0:
                a.append(num)
            elif lose[num] == 1:
                b.append(num)
        for num in win:
            if num not in lose:
                a.append(num)
        return [sorted(a), sorted(b)]