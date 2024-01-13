# 백준 11650 좌표 정렬하기

n = int(input())
list_ = []

for i in range(n):
    a, b = map(int, input().split())
    list_.append([a,b])

list_.sort()

for i in range(n):
    print(str(list_[i][0])+" "+str(list_[i][1]))