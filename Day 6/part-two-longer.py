from sys import argv


def all_different(data):
    for x in range(len(data)):
        for y in range(x + 1, len(data)):
            if data[x] == data[y]:
                return False
    return True


def find_marker(data):
    cur_range = []
    for x in range(14, len(data)):
        cur_range = data[x - 14:x]
        if all_different(cur_range):
            return x


if __name__ == '__main__':
    with open(argv[1]) as file:
        for line in file:
            print(find_marker(line.strip()))
