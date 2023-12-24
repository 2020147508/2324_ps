# 백준 2941 크로아티아 알파벳

given_str = input() # input이 한 줄이면 꼭 sys 할 필요는 없는듯
alph = 0
i = 0

while (i < len(given_str)):
    str_ = given_str[i:i+2]
    if str_ == "c=" or str_ == "c-" or str_ == "d-" or str_ == "lj" or str_ == "nj" or str_ == "s=" or str_ == "z=":
        alph += 1
        i += 2
    elif str_ == "dz":
        # 게시판 보고 해결 : dz=dz 경우
        if i+2 < len(given_str) and given_str[i+2] == "=":
            alph += 1
            i += 3
        else:
            alph += 1
            i += 1
    else:
        alph += 1
        i += 1
print(alph)