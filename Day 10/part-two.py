from sys import argv


cycles = {
        'noop': 1,
        'addx': 2,
    }


def execute_program(program):
    x = 1
    for line in program:
        line = line.split(' ')
        for i in range(cycles[line[0]]):
            yield x
        if line[0] == 'addx':
            x += int(line[1])
    yield x


def print_to_crt(program):
    line = ''
    pos = 0
    execution = execute_program(program)
    for index, x in enumerate(execution):
        pos += 1
        if pos in [x, x + 1, x + 2]:
            line += '#'
        else:
            line += '.'
        if pos % 40 == 0:
            print(line)
            line = ''
            pos = 0


if __name__ == '__main__':
    with open(argv[1]) as file:
            print_to_crt(file.read().split('\n'))
