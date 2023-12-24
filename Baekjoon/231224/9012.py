# 백준 9012 괄호

num_of_inputs = int(input())

for i in range(num_of_inputs):
    pars = input()
    pairs = 0
    for j in range(len(pars)):
        if pairs < 0:
            break
        else:
            if pars[j] == "(":
                pairs += 1
            elif pars[j] == ")":
                pairs -= 1
    if pairs == 0:
        print("YES")
    else:
        print("NO")