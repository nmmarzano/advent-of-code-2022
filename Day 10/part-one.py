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


def execute_and_examine(program):
    signal_sum = 0
    execution = execute_program(program)
    for index, cycle in enumerate(execution):
        if (index + 1) == 20 or (index - 20 + 1) % 40 == 0:
            print(f'{index + 1}: x = {cycle}, signal strength = {(index + 1) * cycle}')
            signal_sum += (index + 1) * cycle
    return signal_sum


if __name__ == '__main__':
    with open(argv[1]) as file:
            print(execute_and_examine(file.read().split('\n')))
