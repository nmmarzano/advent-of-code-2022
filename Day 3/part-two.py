import sys


def get_priority(item):
    priority = ord(item) - ord('A')
    if priority < 27:
        priority += 27
    else:
        priority -= 31
    return priority


def find_badge(packs):
    return set(packs[0]).intersection(set(packs[1])).intersection(set(packs[2])).pop()


if __name__ == '__main__':
    total_priority = 0
    with open(sys.argv[1]) as file:
        lines = file.read().strip().split('\n')
        packs = [[lines[x], lines[x + 1], lines[x + 2]] for x in range(0, len(lines), 3)]
        for group in packs:
            total_priority += get_priority(find_badge(group))

    print(total_priority)
