import cvxpy

subjects = ['Education', 'Security', 'Infrastructures', 'Development']
preferences1 = [['Education', 'Security'], ['Education', 'Development'], ['Education', 'Infrastructures'],
                ['Education', 'Security', 'Development'], ['Security', 'Development']]
preferences2 = [['Education', 'Security', 'Development'], ['Education', 'Infrastructures', 'Development'],
                ['Education', 'Security', 'Infrastructures'], ['Security', 'Infrastructures', 'Development']]
preferences3 = [['Education', 'Security'], ['Education', 'Development'], ['Education', 'Infrastructures'],
                ['Education', 'Security', 'Development'], ['Security', 'Development'], ['Infrastructures']]


def Nash_budget(total: float, subjects: list[str], preferences: list[list[str]]):
    '''
    :param total: the whole budget
    :param subjects: List of subjects
    :param preferences: List of all player preferences
    >>> Nash_budget(500, ['A', 'B', 'C', 'D'], [['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C'], ['A']])
    Allocation: 500
    370.156 for A
    64.922 for B
    64.922 for C
    0.000 for D
    Citizen 0 gives 85.078 to A and 14.922 to B.
    Citizen 1 gives 85.078 to A and 14.922 to C.
    Citizen 2 gives 100.000 to A and 0.000 to D.
    Citizen 3 gives 50.000 to B and 50.000 to C.
    Citizen 4 gives 100.000 to A.
    >>> Nash_budget(total=1000, subjects=subjects, preferences=preferences1)
    Allocation: 1000
    640.381 for Education
    179.809 for Security
    0.000 for Infrastructures
    179.809 for Development
    Citizen 0 gives 156.154 to Education and 43.846 to Security.
    Citizen 1 gives 156.154 to Education and 43.846 to Development.
    Citizen 2 gives 200.000 to Education and 0.000 to Infrastructures.
    Citizen 3 gives 128.076 to Education and 35.962 to Security and 35.962 to Development.
    Citizen 4 gives 100.000 to Security and 100.000 to Development.
    >>> Nash_budget(total=1500, subjects=subjects, preferences=preferences2)
    Allocation: 1500
    375.000 for Education
    375.000 for Security
    375.000 for Infrastructures
    375.000 for Development
    Citizen 0 gives 125.000 to Education and 125.000 to Security and 125.000 to Development.
    Citizen 1 gives 125.000 to Education and 125.000 to Infrastructures and 125.000 to Development.
    Citizen 2 gives 125.000 to Education and 125.000 to Security and 125.000 to Infrastructures.
    Citizen 3 gives 125.000 to Security and 125.000 to Infrastructures and 125.000 to Development.
    >>> Nash_budget(total=2000, subjects=subjects, preferences=preferences3)
    Allocation: 2000
    911.935 for Education
    322.940 for Security
    442.185 for Infrastructures
    322.940 for Development
    Citizen 0 gives 246.161 to Education and 87.172 to Security.
    Citizen 1 gives 246.161 to Education and 87.172 to Development.
    Citizen 2 gives 224.484 to Education and 108.849 to Infrastructures.
    Citizen 3 gives 195.131 to Education and 69.101 to Security and 69.101 to Development.
    Citizen 4 gives 166.667 to Security and 166.667 to Development.
    Citizen 5 gives 333.333 to Infrastructures.
    '''
    alloc = cvxpy.Variable(len(subjects))
    expediency = [None] * len(preferences)
    for element, person in enumerate(preferences):
        temp = None
        for preference in person:
            if temp is not None:
                temp += alloc[subjects.index(preference)]
            else:
                temp = alloc[subjects.index(preference)]
        expediency[element] = temp
    logs = cvxpy.sum([cvxpy.log(elem) for elem in expediency])
    prob = cvxpy.Problem(cvxpy.Maximize(logs), constraints=[cvxpy.sum(alloc) == total] + [0 <= elem for elem in alloc])
    prob.solve()

    print(f'Allocation: {total}')
    for element, sub in enumerate(subjects):
        print(f'{alloc[element].value:.3f} for {sub}')
    contribution = total / len(preferences)
    for citizen, player in enumerate(preferences):
        print(f'Citizen {citizen} gives', end=" ")
        temp = contribution / expediency[citizen].value
        length = len(player)
        for pre in range(0, length):
            contribute = alloc[subjects.index(player[pre])].value * temp
            print(f'{contribute:.3f} to {player[pre]}', end=".\n") if pre == length-1 else print(f'{contribute:.3f} to {player[pre]}', end=" and ")


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())

