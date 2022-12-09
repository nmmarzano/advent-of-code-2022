from sys import argv
from functools import reduce


def count_visible(rows, row, column):
    if row == 0 or column == 0 or row == len(rows) - 1 or column == len(rows[0]) - 1:
        return 0
    
    visible = []

    count = 0
    for x in range(column - 1, -1, -1):
        count += 1
        if rows[row][x] >= rows[row][column]:
            break
    visible.append(count)
            

    count = 0
    for x in range(column + 1, len(rows[0])):
        count += 1
        if rows[row][x] >= rows[row][column]:
            break
    visible.append(count)

    count = 0
    for y in range(row - 1, -1, -1):
        count += 1
        if rows[y][column] >= rows[row][column]:
            break
    visible.append(count)

    count = 0
    for y in range(row + 1, len(rows)):
        count += 1
        if rows[y][column] >= rows[row][column]:
            break
    visible.append(count)
    
    return reduce(lambda a, b: a * b, visible)


def get_max_visible(rows):
    max_visible = 0
    count = 0
    for row in range(len(rows)):
        for column in range(len(rows[row])):
            count = count_visible(rows, row, column)
            if count > max_visible:
                max_visible = count
    return max_visible


if __name__ == '__main__':
    with open(argv[1]) as file:
        data = [[int(x) for x in row] for row in file.read().split('\n')]
        print(get_max_visible(data))
