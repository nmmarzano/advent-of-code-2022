from sys import argv


def get_distance(p1, p2):
    x_distance = abs(p1[0] - p2[0])
    y_distance = abs(p1[1] - p2[1])
    return max(x_distance, y_distance)


def execute_path(directions):
    pos = [[0, 0] for x in range(10)]
    tail_positions = set()

    for direction in directions:
        direction = direction.split(' ')
        for times in range(int(direction[1])):
            if direction[0] == 'R':
                pos[0][0] += 1
            elif direction[0] == 'L':
                pos[0][0] -= 1
            elif direction[0] == 'U':
                pos[0][1] += 1
            elif direction[0] == 'D':
                pos[0][1] -= 1

            for i in range(1, 10):
                if get_distance(pos[i - 1], pos[i]) >= 2:
                    if pos[i - 1][0] > pos[i][0]:
                        pos[i][0] += 1
                    elif pos[i - 1][0] < pos[i][0]:
                        pos[i][0] -= 1
                    if pos[i - 1][1] > pos[i][1]:
                        pos[i][1] += 1
                    elif pos[i - 1][1] < pos[i][1]:
                        pos[i][1] -= 1

            tail_positions.add(f'{pos[9][0]},{pos[9][1]}')
                
    return len(tail_positions)


if __name__ == '__main__':
    with open(argv[1]) as file:
        print(execute_path(file.read().split('\n')))
