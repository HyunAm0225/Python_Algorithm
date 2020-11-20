from collections import deque
n = int(input()) # 정사각형

# 인형뽑기 크레인
board = [list(map(int,input().split())) for i in range(n)]

# move 움직임
move = deque(list(map(int,input().split())))

# 담아질 basket
basket = []
# 답


def input_basket(board, move, basket):
    answer = 0
    while move:
        find_step = move.popleft()
        for i in range(n):
            if board[i][find_step-1] == 0:
                continue
            else:
                basket.append(board[i][find_step-1])
                board[i][find_step-1] = 0
                if len(basket) >1:
                    if basket[len(basket)-1] == basket[len(basket)-2]:
                        answer+=2
                        basket = basket[:-2]
                break
    return answer 
answer = input_basket(board,move,basket)
print(answer)
'''
board
[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
move
[1,5,3,5,1,2,1,4]
'''