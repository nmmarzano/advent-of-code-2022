from sys import argv


def find_marker(data):
    cur_range = []
    for x in range(14, len(data)):
        cur_range = data[x-14:x]
        if len(set(cur_range)) == 14: # hehe
            return x


if __name__ == '__main__':
    with open(argv[1]) as file:
        for line in file:
            print(find_marker(line.strip()))
