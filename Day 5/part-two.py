from sys import argv
import re


def get_last(lists):
    result = ''
    for element in lists:
        result += element[-1]
    return result


def make_movements(lists, movements):
    for movement in movements:
        lists[movement[2] - 1] = lists[movement[2] - 1] + lists[movement[1] - 1][-movement[0]:]
        lists[movement[1] - 1] = lists[movement[1] - 1][:-movement[0]]


def get_lists(stacks):
    lists = [[] for x in range(len(stacks[0]))]

    for row in range(len(stacks) - 1, -1, -1):
        for index, column in enumerate(stacks[row]):
            if column != ' ':
                lists[index].append(column)
    
    return lists


if __name__ == '__main__':
    with open(argv[1]) as file:
        data = file.read().split('\n\n')
    
        data[0] = data[0].split('\n')[:-1]
        
        data[0] = [[x[i] for i in range(1, len(data[0][0]), 4)] for x in data[0]]
        data[1] = [list(map(lambda x: int(x), re.findall(r'\d+', x))) for x in data[1].split('\n')]
        
        lists = get_lists(data[0])
        make_movements(lists, data[1])

        print(get_last(lists))
