# 백준 2563 색종이

num_of_paper = int(input())
total_paper = [[0 for i in range(100)] for j in range(100)]

for i in range(num_of_paper):
    list_ = list(map(int, input().split()))
    for j in range(10):
        for k in range(10):
            total_paper[list_[1]+j][list_[0]+k] = 1
area = 0
for i in range(100):
    for j in range(100):
        area += total_paper[i][j]
print(area)