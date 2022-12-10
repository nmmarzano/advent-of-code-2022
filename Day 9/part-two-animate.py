from sys import argv
import pygame
import time


WIDTH = 1000
HEIGHT = 1000


NODES = 100


def get_distance(p1, p2):
    x_distance = abs(p1[0] - p2[0])
    y_distance = abs(p1[1] - p2[1])
    return max(x_distance, y_distance)


def execute_path(directions):
    pos = [[0, 0] for x in range(NODES)]
    tail_positions = set()

    surface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Rope Physics')

    for direction in directions:
        direction = direction.split(' ')
        for times in range(int(direction[1])):

            surface.fill((0, 0, 0))
            
            if direction[0] == 'R':
                pos[0][0] += 1
            elif direction[0] == 'L':
                pos[0][0] -= 1
            elif direction[0] == 'U':
                pos[0][1] += 1
            elif direction[0] == 'D':
                pos[0][1] -= 1

            for i in range(1, NODES):
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

        pygame.draw.lines(surface, (255, 255, 255), False, list(map(lambda a: [a[0] * 3 + WIDTH/2, a[1] * 3 + HEIGHT/2], pos)), 5)
        pygame.display.update()
        time.sleep(0.01)
                
    return len(tail_positions)


if __name__ == '__main__':
    pygame.init()
    with open(argv[1]) as file:
        print(execute_path(file.read().split('\n')))
    pygame.quit()
