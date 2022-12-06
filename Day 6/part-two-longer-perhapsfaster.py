from sys import argv


range_length = 14


def find_after_repeat(data):
    for x in range(len(data), -1, -1):
        for y in range(x + 1, len(data)):
            if data[x] == data[y]:
                return x + 1
    return 0


def find_marker(data):
    cur_range = data[0:range_length]
    prev_x = 0
    x = find_after_repeat(cur_range)
    while x != prev_x:
        prev_x = x
        cur_range = data[x:x+ range_length]
        x += find_after_repeat(cur_range)
    return x + range_length


if __name__ == '__main__':
    with open(argv[1]) as file:
        for line in file:
            print(find_marker(line.strip()))
