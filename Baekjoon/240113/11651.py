# 백준 11651 좌표 정렬하기 2

# 질문 게시판 보고 해결

n = int(input())
list_ = []

for i in range(n):
    a, b = map(int, input().split())
    list_.append([a,b])

list_.sort(key=lambda x:(x[1], x[0])) # y값이 같은 경우에 첫 번째 값을 기준으로 오름차순 정렬하도록 코드 추가

for i in range(n):
    print(str(list_[i][0])+" "+str(list_[i][1]))