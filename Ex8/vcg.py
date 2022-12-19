import doctest
from itertools import permutations
import math
INF = math.inf


def make_list(without: False, index: int, values: list[list], players_options: list):
    res = []
    for i in range(0, len(players_options)):
        sum = 0
        for j in range(0, len(values)):
            if without:
                if index != players_options[i][j]:
                    sum += values[players_options[i][j]][j]
            else:
                sum += values[players_options[i][j]][j]
        res.append(sum)
    return res


def best_option(options: list):
    best = -1
    m = -INF
    for i in range(0, len(options)):
        if m < options[i]:
            m, best = options[i], i
    return best, m


def VCG(matrix: list[list]):
    """
    >>> [VCG([[5, 10], [6, 9]])]
    [['Player 0 ---> Obj: 1 Price: 3', 'Player 1 ---> Obj: 0 Price: 0']]
    >>> [VCG([[7, 15], [9, 11]])]
    [['Player 0 ---> Obj: 1 Price: 2', 'Player 1 ---> Obj: 0 Price: 0']]
    >>> [VCG([[6, 9, 12], [5, 10, 9], [8, 12, 10]])]
    [['Player 0 ---> Obj: 2 Price: 3', 'Player 1 ---> Obj: 1 Price: 4', 'Player 2 ---> Obj: 0 Price: 0']]
    >>> [VCG([[7, 8, 10], [8, 10, 9], [8, 9, 10]])]
    [['Player 0 ---> Obj: 2 Price: 2', 'Player 1 ---> Obj: 1 Price: 1', 'Player 2 ---> Obj: 0 Price: 0']]
    >>> [VCG([[5, 7, 8, 7], [10, 5, 7, 9], [8, 6, 11, 10], [12, 5, 9, 7]])]
    [['Player 0 ---> Obj: 1 Price: 0', 'Player 1 ---> Obj: 3 Price: 0', 'Player 2 ---> Obj: 2 Price: 1', 'Player 3 ---> Obj: 0 Price: 1']]
    """
    players_num = []
    for i in range(0, len(matrix)):
        players_num.append(i)
    players_options = list(permutations(players_num))

    without_list = []
    for index in range(0, len(matrix)):
        sum = make_list(without=True, index=index, values=matrix, players_options=players_options)
        without_list.append(sum)

    best_without = []
    for index in range(0, len(without_list)):
        curr_b, curr_m = best_option(without_list[index])
        best_without.append((curr_b, curr_m))

    options = make_list(without=False, index=0, values=matrix, players_options=players_options)
    best, m = best_option(options)
    res = []
    for index in range(0, len(best_without)):
        p = best_without[index][1] - without_list[index][best]
        res.append("Player " + str(index) + " ---> Obj: " + str(players_options[best].index(index)) + " Price: " + str(p))
    return res


if __name__ == "__main__":
    print(doctest.testmod())
    print(VCG([[5, 10], [6, 9]]))
    print(VCG([[6, 9, 12], [5, 10, 9], [8, 12, 10]]))
