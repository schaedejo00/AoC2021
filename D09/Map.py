from queue import Queue

import numpy as np


class Map:

    def __init__(self, map: list[list[int]]):
        self.map = map

    def isLowPoint(self, x: int, y: int) -> bool:
        value = self.map[x][y]
        neighbours = self.getNeighbours((x, y))
        for neighbour in neighbours:
            if value >= self.map[neighbour[0]][neighbour[1]]:
                return False
        return True

    def getLowPointList(self) -> list[(int, int)]:
        result = []
        for x in range(0, len(self.map)):
            for y in range(0, len(self.map[1])):
                if self.isLowPoint(x, y):
                    result.append((x, y))
        return result

    def isIndexInBounds(self, point: (int, int)) -> bool:
        x = point[0]
        y = point[1]
        return x >= 0 and y >= 0 and x < len(self.map) and y < len(self.map[0])

    def getMap(self) -> list[list[int]]:
        return self.map

    def getBasinSize(self, point: (int, int)) -> int:
        neighbours = Queue()
        [neighbours.put(n) for n in self.getNeighbours(point)]

        checked: list[(int, int)] = [point]
        basin: list[(int, int)] = [point]
        while not neighbours.empty():
            neighbour = neighbours.get()
            if neighbour not in checked and self.map[neighbour[0]][neighbour[1]] < 9:
                basin.append(neighbour)
                [neighbours.put(n) for n in self.getNeighbours(neighbour) if n not in checked]
            checked.append(neighbour)
        #print("basin", point, basin)
        return len(basin)

    def getNeighbours(self, point: (int, int)) -> list[(int, int)]:
        xDiff = [-1, 0, 0, 1]
        yDiff = [0, -1, 1, 0]
        x = point[0]
        y = point[1]
        neighbours: [(int, int)] = []
        for i in range(0, len(xDiff)):
            xToCheck = x + xDiff[i]
            yToCheck = y + yDiff[i]
            if self.isIndexInBounds((xToCheck, yToCheck)):
                neighbours.append((xToCheck, yToCheck))
        return neighbours
