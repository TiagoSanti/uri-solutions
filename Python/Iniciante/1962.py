N = int(input())

for i in range(N):
    T = int(input())

    if T == 2015:
        print('1 A.C.')
    elif T < 2015:
        print('{} D.C.'.format(2015 - T))
    else:
        print('{} A.C.'.format(T - 2014))
