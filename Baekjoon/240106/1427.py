# 백준 1427 소트인사이드

n = list(map(int, input()))

n.sort(reverse=True)

print(''.join(str(s) for s in n))