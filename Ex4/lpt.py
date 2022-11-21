

def lpt(m: int, lst: list) -> dict:
    print(f'for {m} machines: ')
    d = dict()
    for c in range(1, m+1):
        d[c] = []
    # print(d)
    count = 1
    up = True
    for e in lst:
        s = d[count]
        # print(count, s)
        s.append(e)
        d[count] = s
        # print(d)
        if up:
            count += 1
        else:
            count -= 1
        if count == m+1 or count == 0:
            if up:
                up = False
                count = m
            else:
                up = True
                count = 1

    s = 0
    max = 0
    for i in d:
        cs = sum(d[i])
        s += cs
        if max < cs:
            max = cs

    opt = s/m
    print(f'-> OPT: {opt}')
    print(f'-> MAX LPT: {max}')
    print(f'-> Approximation: {max/opt}')
    lpt_costs = 4/3 - 1/(3*m)
    print(f'-> lpt_costs: {lpt_costs}')

    print(d)
    print('-----------------------------------------------\n')





if __name__ == '__main__':
    l1 = [13,11, 9, 9, 8, 7, 7, 6, 6, 5, 5, 4, 4, 4]
    print('\n')
    lpt(4, l1)
    lpt(5, l1)
    lpt(6, l1)
    lpt(7, l1)
    lpt(8, l1)
    lpt(9, l1)

