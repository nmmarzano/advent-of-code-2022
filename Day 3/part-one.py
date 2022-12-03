import sys


def get_priority(item):
    priority = ord(item) - ord('A')
    if priority < 27:
        priority += 27
    else:
        priority -= 31
    return priority


def find_repeated_item(line):
    left, right = set(line[:len(line)//2]), set(line[len(line)//2:])
    return left.intersection(right).pop()


if __name__ == '__main__':
    total_priority = 0
    with open(sys.argv[1]) as file:
        for line in file:
            if line.strip():
                total_priority += get_priority(find_repeated_item(line.strip()))

    print(total_priority)
