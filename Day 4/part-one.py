import sys


def is_either_contained(range_1, range_2):
    first_l, first_r = map(lambda a: int(a), range_1.split('-'))
    second_l, second_r = map(lambda a: int(a), range_2.split('-'))
    
    return (first_l <= second_l and first_r >= second_r) or (second_l <= first_l and second_r >= first_r)


if __name__ == '__main__':
    count = 0

    with open(sys.argv[1]) as file:
        for line in file:
            if is_either_contained(*line.strip().split(',')):
                count += 1

    print(count)
