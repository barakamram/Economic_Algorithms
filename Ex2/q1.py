import doctest

class Agent:

    def __init__(self, values: list):
        self.values = values

    def value(self, option: int) -> float:
        """
         INPUT: the index of an option.
         OUTPUT: the value of the option to the agent.
        """
        return self.values[option]


def isParetoImprovement(agents: list[Agent], option1: int, option2: int) -> bool:
    """
    >>> isParetoImprovement(agents, 3,2)
    True
    >>> isParetoImprovement(agents, 1,2)
    False
    >>> isParetoImprovement(agents, 1,1)
    False
    """
    # check if option1 equal option2: if 'True' return 'False'
    if option1 == option2:
        return False
    # check for each player if he prefer option2 than option1.
    for a in agents:
        if a.value(option1) < a.value(option2):
            return False
    return True


def isParetoOptimal(agents: list[Agent], option: int, allOptions: list[int]) -> bool:
    """
    >>> isParetoOptimal(agents, 1, all_options)
    True
    >>> isParetoOptimal(agents, 2, all_options)
    False
    >>> isParetoOptimal(agents, 3, all_options)
    True
    >>> isParetoOptimal(agents, 4, all_options)
    True
    >>> isParetoOptimal(agents, 5, all_options)
    True
    """
    # check if there is better option than all options.
    for o in allOptions:
        if isParetoImprovement(agents, o, option) and o != option:
            return False
    return True


if __name__ == '__main__':
    barak = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
    tal = {1: 3, 2: 1, 3: 2, 4: 5, 5: 4}
    maayan = {1: 3, 2: 5, 3: 5, 4: 1, 5: 1}
    agents = [Agent(barak), Agent(tal), Agent(maayan)]
    all_options = [1, 2, 3, 4, 5]
    doctest.testmod()