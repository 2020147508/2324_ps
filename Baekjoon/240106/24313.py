# 백준 24313 알고리즘 수업 - 점근적 표기 1

a, b = map(int, input().split())
c = int(input())
n_zero = int(input())

if (c-a < 0):
    print(0)
elif (c-a == 0):
    if b <= 0:
        print(1)
    else:
        print(0)
else:
    if (c-a) * n_zero - b >= 0:
        print(1)
    else:
        print(0)