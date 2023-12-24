# 백준 25206 너의 평점은

import sys

lines = sys.stdin.readlines()
score_dict = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0, "F":0.0}
s = 0
m = 0
for line in lines:
    list_ = list(map(str, line.split()))
    if list_[2] in score_dict:
        score = score_dict[list_[2]]
        s += float(list_[1]) * score
        m += float(list_[1])
    else:
        continue
print(s/m)