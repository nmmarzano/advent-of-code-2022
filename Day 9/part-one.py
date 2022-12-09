from sys import argv


def get_distance(p1, p2):
    x_distance = abs(p1[0] - p2[0])
    y_distance = abs(p1[1] - p2[1])
    return max(x_distance, y_distance)


def execute_path(directions):
    h_pos = [0, 0]
    t_pos = [0, 0]
    tail_positions = set()

    for direction in directions:
        direction = direction.split(' ')
        for times in range(int(direction[1])):
            if direction[0] == 'R':
                h_pos[0] += 1
            elif direction[0] == 'L':
                h_pos[0] -= 1
            elif direction[0] == 'U':
                h_pos[1] += 1
            elif direction[0] == 'D':
                h_pos[1] -= 1

            if get_distance(h_pos, t_pos) >= 2:
                if h_pos[0] > t_pos[0]:
                    t_pos[0] += 1
                elif h_pos[0] < t_pos[0]:
                    t_pos[0] -= 1
                if h_pos[1] > t_pos[1]:
                    t_pos[1] += 1
                elif h_pos[1] < t_pos[1]:
                    t_pos[1] -= 1

            tail_positions.add(f'{t_pos[0]},{t_pos[1]}')
                
    return len(tail_positions)


if __name__ == '__main__':
    with open(argv[1]) as file:
        print(execute_path(file.read().split('\n')))
