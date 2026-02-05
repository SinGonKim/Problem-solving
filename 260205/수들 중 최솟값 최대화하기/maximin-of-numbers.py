import sys
INF = sys.maxsize
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
answer = 0
# Please write your code here.

def solution(row, prev_cols, cnt):
    global answer
    if row == n:
        answer = max(answer, cnt)
        return
    
    res_col = list(set([i for i in range(n)]) - set(prev_cols))

    for col in res_col:
        prev_cols.append(col)
        solution(row+1, prev_cols, min(cnt, grid[row][col]))
        prev_cols.pop()

solution(0,[],INF)
print(answer)