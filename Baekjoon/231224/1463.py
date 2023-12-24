# 백준 1463 1로 만들기

# 질문 게시판 보고 해결

num = int(input())
data = [0 for i in range(10**6)]
data[1] = 1
data[2] = 1

def check(num):
    if num == 1 or num == 2 or num == 3:
        return data[num-1]
    
    # 일단 top-down 방식이므로 이전에 계산했을 수도 있으므로 이게 나와줘야 함 : 바로 끝날 수 있게
    if data[num-1] != 0:
        return data[num-1]
    
    # 각각의 경우에서 바로 계산하고 array를 채울 수 있도록 해주기.
    # 이전 코드는 너무 return 하기 전에 recursion을 깊이 돌아야 해서 채워진 게 하나도 없는 상태였음
    # 모든 경우를 한 번에 계산하려고 하지 말고 각각 경우의 수 나눠서 각각 계산
    
    if num % 6 == 0:
        data[num-1] = min(check(int(num/2)), check(int(num/3))) + 1
    
    elif num % 2 == 0:
        data[num-1] = min(check(int(num/2)), check(num-1)) + 1
    
    elif num % 3 == 0:
        data[num-1] = min(check(int(num/3)), check(num-1)) + 1

    else:
        data[num-1] = check(num-1)+1

    return data[num-1]
    
    '''
    can_two = math.inf
    if (num % 2 == 0):
        if (data[int(num/2)-1] != 0):
            can_two = data[int(num/2)-1] + 1
        else:
            can_two = check(int(num/2)) + 1

    can_three = math.inf
    if (num % 3 == 0):
        if (data[int(num/3)-1] != 0):
            can_three = data[int(num/3)-1] + 1
        else:
            can_three = check(int(num/3)) + 1

    if (data[num-2] != 0):
        can_one = data[num-2]+1
    else:
        can_one = check(num-1) + 1

    return_val = min(can_one, can_two, can_three)
    data[num-1] = return_val

    return return_val
    '''

print(check(num))