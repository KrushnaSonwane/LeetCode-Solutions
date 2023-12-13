class Robot:

    def __init__(self, width: int, height: int):
        self.i, self.A = 0, []
        for j in range(width):
            self.A.append([j, 0, 'East'])
        for j in range(1, height):
            self.A.append([width-1, j, 'North'])
        for j in range(width-2, -1, -1):
            self.A.append([j, height-1, 'West'])
        for j in range(height-2, 0, -1):
            self.A.append([0, j, "South"])
        self.start = False

    def step(self, num: int) -> None:
        self.i += num
        self.start = True

    def getPos(self) -> List[int]:
        x, y, _ = self.A[self.i%len(self.A)]
        return [x, y]

    def getDir(self) -> str:
        if not self.start:
            return 'East'
        else:
            if self.i % len(self.A) == 0: return 'South'
            return self.A[self.i%len(self.A)][2]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()