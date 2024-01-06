# 백준 2751 수 정렬하기 2

import sys
n = int(sys.stdin.readline()) # 시간초과 나서 input()에서 sys.stdin.readline()으로 변경

list_ = []

for i in range(n):
    list_.append(int(sys.stdin.readline())) # 시간초과 나서 input()에서 sys.stdin.readline()으로 변경

list_ = sorted(list_)

for i in range(len(list_)):
    print(str(list_[i]))