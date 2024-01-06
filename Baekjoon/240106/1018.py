# 백준 1018 체스판 다시 칠하기

a, b = map(int, input().split())
chess_board = []

for i in range(a):
    line = list(input())
    chess_board.append(line)

ans_w = []
ans_b = []
for i in range(4):
    ans_w.append(['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'])
    ans_w.append(['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'])
    ans_b.append(['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'])
    ans_b.append(['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'])

score = 64

for i in range(a-7):
    for j in range(b-7):
        w_score = 0
        b_score = 0
        min_score = 0
        mid_curr_box = chess_board[i:i+8][:]
        curr_box = []
        for k in range(8):
            curr_box.append(mid_curr_box[k][j:j+8])
        for k in range(8):
            for l in range(8):
                if curr_box[k][l] != ans_w[k][l]:
                    w_score += 1
                if curr_box[k][l] != ans_b[k][l]:
                    b_score += 1
        min_score = min(w_score, b_score)
        if min_score < score:
            score = min_score
print(score)