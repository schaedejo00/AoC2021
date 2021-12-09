from collections import defaultdict
from typing import List

import numpy as np

from D05.Point import Point

from Map import Map

#with open('example.txt', 'r', encoding="utf-8") as f:
with open('input_1.txt', 'r', encoding="utf-8") as f:
    puzzleInput = f.read().split("\n")

heightMap = Map([[int(n) for n in list(line)] for line in puzzleInput])

print(heightMap.getMap())

lowPoints = heightMap.getLowPointList()

riskLevel = 0
for point in lowPoints:
    pX, pY = point
    riskLevel = riskLevel + heightMap.getMap()[pX][pY] + 1
print(riskLevel, lowPoints)

