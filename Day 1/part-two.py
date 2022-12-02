import sys
from functools import reduce


def find_top_three_calories(data):
    current_count = 0
    current_most = [0, 0, 0]
    min_of_most = 0
    for line in data:
        if line == '':
            min_of_most = min(current_most)
            if current_count > min_of_most:
                current_most[current_most.index(min_of_most)] = current_count
            current_count = 0
        else:
            current_count += int(line)
    return current_most


if __name__ == '__main__':
    with open(sys.argv[1]) as file:
        top_three_calories = find_top_three_calories(file.read().split('\n'))
        print(reduce(lambda a, b: a + b, top_three_calories))
