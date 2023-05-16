class Solution(object):
    def minimumCost(self, start, target, specialRoads):
        useIt = []
        for x1, y1, x2, y2, c in specialRoads:
            currCost = abs(x1 - x2) + abs(y1 - y2)
            if currCost > c:
                useIt.append([x1, y1, x2, y2, c])
        queue, dist = [[0, start[0], start[1]]], {}
        heapq.heapify(queue)
        while queue:
            cost, x1, y1 = heapq.heappop(queue)
            if [x1, y1] == target: return cost
            if (x1, y1) in dist and dist[(x1, y1)] <= cost: continue
            dist[(x1, y1)] = cost
            x2, y2 = target
            heapq.heappush(queue, [cost + abs(x1 - x2) + abs(y1 - y2), x2, y2])
            for x, y, xx, yy, c in useIt:
                heapq.heappush(queue, [cost + c + abs(x1 - x) + abs(y1 - y), xx, yy])
        return -1