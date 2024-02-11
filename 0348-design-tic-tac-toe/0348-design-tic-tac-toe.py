class TicTacToe:

    def __init__(self, n: int):
        self.D1 = {(i, i) for i in range(n)}
        self.D2 = {(i, (n - (i + 1))) for i in range(n)}
        self.p1C, self.p1R, self.p2C, self.p2R = Counter(), Counter(), Counter(), Counter()
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        if player == 1:
            a, b = self.p1R, self.p1C
        else:
            a, b = self.p2R, self.p2C
        a[row] += 1
        b[col] += 1
        if (row, col) in self.D1:
            a['D1'] += 1
        if (row, col) in self.D2:
            a['D2'] += 1
        res = 0
        for size in [a[row], b[col], a['D1'], a['D2']]:
            if size == self.n:
                res = player
        return res

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)