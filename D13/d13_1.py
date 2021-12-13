import numpy as np
import matplotlib.pyplot as plt


#with open('example.txt', 'r', encoding="utf-8") as f:
with open('input_1.txt', 'r', encoding="utf-8") as f:
    puzzleInput = f.read().split("\n")

coords: list[list[int]] = [[int(n) for n in line.split(",")] for line in puzzleInput if "," in line]
xs: [int] = [line[0] for line in coords]
ys: [int] = [line[1] for line in coords]

folds: [] = [[n for n in line[11:].split("=")]  for line in puzzleInput if line.startswith("fold along ")]
print(coords, folds)

field: list[list[int]] =np.zeros((np.max(ys)+1, np.max(xs)+1), int)


for coord in coords:
    x, y = coord
    field[y][x] += 1

print(np.count_nonzero(field))
plt.imshow(field, interpolation='none')
plt.show()

for fold in folds:
    dir, border = fold
    border = int(border)
    if dir == 'y':
        new_field = field[0:border]
        to_fold = field[(border + 1):]
        #print(dir, border, len(field), len(new_field), len(to_fold))
        max_y = len(new_field) - 1
        for y in range(0, len(to_fold)):
            for x in range(0, len(to_fold[0])):
                n_y = max_y - y
                if to_fold[y][x] == 1:
                    new_field[n_y][x] = 1
        field = new_field
        #print(dir, border, np.count_nonzero(field))
    if dir == 'x':
        new_field = [[line[i] for i in range(0, len(line)) if i < border] for line in field]
        to_fold = [[line[i] for i in range(0, len(line)) if i > border] for line in field]
        #print(dir, border, len(field[0]), len(new_field[0]), len(to_fold[0]))
        max_x = len(new_field[0]) - 1
        for y in range(0, len(to_fold)):
            for x in range(0, len(to_fold[0])):
                n_x = max_x - x
                if to_fold[y][x] == 1:
                    #if new_field[y][n_x] == 1:
                    #    print((x, y), "->", (n_x, y))
                    new_field[y][n_x] = 1

        field = new_field
        #print(dir, border, np.count_nonzero(field))

#print(field)

plt.imshow(field, interpolation='none')
plt.show()

print(np.count_nonzero(field))


