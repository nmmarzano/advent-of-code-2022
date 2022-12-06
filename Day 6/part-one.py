from sys import argv


def find_marker(data):
    cur_range = []
    for x in range(4, len(data)):
        cur_range = data[x-4:x]
        # if len(set(cur_range)) == 4: ...would be prettier, but this faster!
        if cur_range[0] != cur_range[1] and cur_range[0] != cur_range[2] and cur_range[0] != cur_range[3] and cur_range[1] != cur_range[2] and cur_range[1] != cur_range[3] and cur_range[2] != cur_range[3]:
            return x
    


if __name__ == '__main__':
    with open(argv[1]) as file:
        print(find_marker(file.read().strip()))
