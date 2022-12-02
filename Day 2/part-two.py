from sys import argv

matchup_scores = {
        'X': 0,
        'Y': 3,
        'Z': 6
    }
scores = {
        'A': { # rock
                'X': 3, # scissors
                'Y': 1, # rock
                'Z': 2 # paper
            },
        'B': { # paper
                'X': 1, # rock
                'Y': 2, # paper
                'Z': 3 # scissors
            },
        'C': { # scissors
                'X': 2, # paper
                'Y': 3, # scissors
                'Z': 1 # rock
            }
    }


def calculate_score(data):
    score = 0
    opponent = ''
    me = ''
    for line in file:
            opponent, me = line.strip().split(' ')
            score += matchup_scores[me] + scores[opponent][me]

    return score


if __name__ == '__main__':
    with open(argv[1]) as file:
        print(calculate_score(file))
