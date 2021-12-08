from collections import defaultdict
from typing import List

import numpy as np

from D05.Point import Point


def addDigitToDict(digit: str, dictionary:dict()) -> dict():
    digitLength = len(digit)
    if digitLength == 2:
        dictionary[digit] = [1]
    elif digitLength == 3:
        dictionary[digit] = [7]
    elif digitLength == 4:
        dictionary[digit] = [4]
    elif digitLength == 5:
        dictionary[digit] = [2, 3, 5]
    elif digitLength == 6:
        dictionary[digit] = [0, 6, 9]
    elif digitLength == 7:
        dictionary[digit] = [8]
    return dictionary


# with open('example.txt', 'r', encoding="utf-8") as f:
with open('input_1.txt', 'r', encoding="utf-8") as f:
    puzzleInput = f.read().split("\n")

counter = 0
for line in puzzleInput:
    signalArr, outputArr = [["".join(sorted(digit)) for digit in token.strip().split(" ")] for token in
                            line.strip().split("|")]
    newDict = defaultdict(list)
    for digit in signalArr:
        newDict = addDigitToDict(digit, newDict)

    for token in outputArr:
        numbers = newDict.get(token)
        if len(numbers) == 1 and numbers[0] in [1, 4, 7, 8]:
            counter += 1
print(counter)
