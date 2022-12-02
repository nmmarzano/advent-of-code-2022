from sys import argv

scores = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }
matchup_scores = {
        'A': {
                'X': 3,
                'Y': 6,
                'Z': 0
            },
        'B': {
                'X': 0,
                'Y': 3,
                'Z': 6
            },
        'C': {
                'X': 6,
                'Y': 0,
                'Z': 3
            }
    }


def calculate_score(data):
    score = 0
    opponent = ''
    me = ''
    for line in file:
            opponent, me = line.strip().split(' ')
            score += scores[me] + matchup_scores[opponent][me]

    return score


if __name__ == '__main__':
    with open(argv[1]) as file:
        print(calculate_score(file))
