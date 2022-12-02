import sys


def find_most_calories(data):
    if data[-1] != '':
        data.append('')
    current_count = 0
    current_most = 0
    for line in data:
        if line == '':
            if current_count > current_most:
                current_most = current_count
            current_count = 0
        else:
            current_count += int(line)
    return current_most


if __name__ == '__main__':
    with open(sys.argv[1]) as file:
        print(find_most_calories(file.read().split('\n')))
