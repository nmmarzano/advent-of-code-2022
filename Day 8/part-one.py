from sys import argv


def is_visible(rows, row, column):
    if row == 0 or column == 0 or row == len(rows) - 1 or column == len(rows[0]) - 1:
        return True

    blocked = False
    for x in range(0, column):
        if rows[row][x] >= rows[row][column]:
            blocked = True
            break
    if not blocked:
        return True

    blocked = False
    for x in range(column + 1, len(rows[0])):
        if rows[row][x] >= rows[row][column]:
            blocked = True
            break
    if not blocked:
        return True

    blocked = False
    for y in range(0, row):
        if rows[y][column] >= rows[row][column]:
            blocked = True
            break
    if not blocked:
        return True

    blocked = False
    for y in range(row + 1, len(rows)):
        if rows[y][column] >= rows[row][column]:
            blocked = True
            break
    if not blocked:
        return True

    return False


def count_visible(rows):
    count = 0
    for row in range(len(rows)):
        for column in range(len(rows[row])):
            if is_visible(rows, row, column):
                count += 1
    return count


if __name__ == '__main__':
    with open(argv[1]) as file:
        data = [[int(x) for x in row] for row in file.read().split('\n')]
        print(count_visible(data))
