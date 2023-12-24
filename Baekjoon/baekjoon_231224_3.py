#백준 1316 그룹 단어 체커

iter_ = int(input())
num_group_vocab = 0

for i in range(iter_):
    str = input()
    not_group_vocab = 0
    check = [-1 for k in range(26)]
    for j in range(len(str)):
        if (not_group_vocab == 0):
            curr = ord(str[j])
            list_index = curr-97 # 아마 sys.stdin.readline() 하면 .rstrip()을 하지 않는 이상 개행 같이 들어옴 -> IndexError 그래서 난 듯!!
            if (check[list_index] == -1):
                check[list_index] = j
            elif (check[list_index] == j-1):
                check[list_index] += 1
            else:
                not_group_vocab = 1
        else:
            break
    if (not_group_vocab == 0):
        num_group_vocab += 1
        
print(num_group_vocab)