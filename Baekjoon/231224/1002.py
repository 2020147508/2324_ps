#백준 1002 터렛

import sys, math

iter_ = int(sys.stdin.readline())
# iter_ = int(input())

for i in range(iter_):
    line = sys.stdin.readline()
    # line = input()
    list_ = list(map(int, line.split()))
    f_x = list_[0]
    f_y = list_[1]
    s_x = list_[3]
    s_y = list_[4]
    f_len = list_[2]
    s_len = list_[5]
    dist_ = math.pow((f_x-s_x),2) + math.pow((f_y-s_y),2)
    dist = math.sqrt(dist_)
    comp = f_len + s_len
    if (f_x == s_x and f_y == s_y and f_len == s_len):
        print(-1)
    elif (max(f_len, s_len) > dist):
        if (max(f_len, s_len) == min(f_len, s_len)+dist):
            print(1)
        elif (max(f_len, s_len)-dist < min(f_len, s_len)):
            print(2)
        elif (max(f_len, s_len)-dist > min(f_len, s_len)):
            print(0)
    else:
        if (dist == comp):
            print(1)
        elif (dist < comp):
            print(2)
        elif (dist > comp):
            print(0)
