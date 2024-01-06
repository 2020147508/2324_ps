# 백준 2839 설탕 배달

n = int(input())

if n % 5 == 0:
    print(n // 5)
else:
    min_result = 5000
    max_ = n // 5
    for i in range(1, max_+1):
        left = n - 5 * i
        if (left % 3 == 0):
            min_result = min(min_result, i + left // 3)
        else:
            continue
    if min_result == 5000:
        if (n % 3 == 0):
            print(n // 3)
        else:
            print(-1)
    else:
        print(min_result)