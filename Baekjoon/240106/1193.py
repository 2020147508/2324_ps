# 백준 1193 분수찾기

n = int(input())

total_num = 0
curr_num = 0

for i in range(10000000):
    if curr_num >= n:
        total_num = i+1
        break
    else:
        curr_num += (i+1)
        continue

diff = curr_num - n
front = 0

if total_num % 2 != 0: # total_num이 홀수일때
    front = total_num - 1 - diff 
else: # total_num이 짝수일때
    front = 1 + diff

back = total_num - front
print(str(front)+"/"+str(back))