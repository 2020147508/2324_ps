# 백준 1005 ACM Craft
# 23.12.24 시간초과
# 

n = int(input())

def min_time(dest, list_of_buildings, buil, min_time_list):
    if (min_time_list[dest] != -1):
        return min_time_list[dest]
    
    # 현재 목표하는 건물만 짓기 위해 걸리는 시간
    time_to_build = list_of_buildings[dest]
    # 현재 목표하는 건물들의 이전 건물들 list
    prev_builds = buil[dest][0]


    max_build_time = -1
    # 현재 목표하는 건물들의 이전 건물들 중 최대의 building time을 가지는 건물의 building time 찾기
    for prev_ in prev_builds:
        if min_time(prev_, list_of_buildings, buil, min_time_list) > max_build_time:
            max_build_time = min_time(prev_, list_of_buildings, buil, min_time_list)

    min_time_list[dest] = max_build_time + time_to_build

    return min_time_list[dest]




for i in range(n):

    N, K = map(int, input().split())
    # 각각의 건물들의 건설시간 list
    list_of_buildings = list(map(int, input().split()))
    # 각각의 건물들의 이전 건물, 이후 건물 list
    buil = [[[], []] for q in range(N)]
    # 각각의 건물들을 짓는 데 걸리는 최소 시간 list
    min_time_list = [-1 for m in range(N)]

    # 각각의 건물들의 이전 건물, 이후 건물 list 채우기
    for j in range(K):
        prev, after = map(int, input().split())
        buil[prev-1][1].append(after-1)
        buil[after-1][0].append(prev-1)

    # 최종 건물
    dest = int(input())

    # 이전 건물이 없는 건물들의 최소시간 = 자기자신의 건설시간
    for e in range(len(buil)):
        if buil[e][0] == []:
            min_time_list[e] = list_of_buildings[e]
            
    print(min_time((dest-1), list_of_buildings, buil, min_time_list))
