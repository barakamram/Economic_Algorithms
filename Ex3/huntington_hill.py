from math import sqrt


def prediction(ls, s):
    sum = 0
    for x in ls:
        sum += x
    p = sum/s
    print(f'--- prediction: ---')
    for x in ls:
        print(f'--- {x} ---> accurate: {x/p}, should get: {int(x/p+0.5)}')
    print('\n')


def make_dict(ls, s):
    d = {}
    for x in ls:
        d[x] = 0
    huntington_hill(d, s)


def huntington_hill(d, s):
    tmp_dct = {}
    for v in d:
        c = d[v]
        if c != 0:
            tmp_dct[v/sqrt(c * (c + 1))] = c
        else:
            tmp_dct[v] = c
    for v in tmp_dct:
        if v == max(tmp_dct):
            w = sqrt(tmp_dct[v]*(tmp_dct[v]+1))
            tmp_dct[v] += 1
            if w != 0.0:
                d[int(v*w+0.5)] += 1
            else:
                d[v] += 1
    print(tmp_dct)
    ss = 0
    for x in d.values():
        ss += x
    if ss == s:
        print(f'--- huntington_hill ---> {d}')
        return
    else:
        huntington_hill(d, s)


if __name__ == '__main__':
    lst1 = [5550, 1450]
    sits1 = 7
    make_dict(lst1, sits1)
    prediction(lst1, sits1)

    lst2 = [3765, 1235]
    sits2 = 10
    make_dict(lst2, sits2)
    prediction(lst2, sits2)

    lst3 = [50102, 18940]
    sits3 = 20
    make_dict(lst3, sits3)
    prediction(lst3, sits3)

    lst4 = [50102, 18840]
    sits4 = 20
    make_dict(lst4, sits4)
    prediction(lst4, sits4)

    # lst5 = [5012, 2560, 995, 3315]
    # sits5 = 20
    # make_dict(lst5, sits5)
    # prediction(lst5, sits5)
    #
    # lst6 = [5572, 23570, 10738, 16545, 3758]
    # sits6 = 50
    # make_dict(lst6, sits6)
    # prediction(lst6, sits6)
    #
    # lst7 = [55672, 234570, 94395, 170532, 42987, 14150]
    # sits7 = 120
    # make_dict(lst7, sits7)
    # prediction(lst7, sits7)
