class SnapshotArray:

    def __init__(self, length: int):
        self.id = 0
        self.hashT = [[[0, 0]] for _ in range(length)]
        
    def set(self, index: int, val: int) -> None:
        self.hashT[index].append([self.id, val])

    def snap(self) -> int:
        self.id += 1
        return self.id - 1

    def get(self, index: int, snap_id: int) -> int:
        ind = bisect.bisect_right(self.hashT[index], [snap_id, 10 ** 9])
        return self.hashT[index][ind - 1][1]