n = int(input())
num = [list(map(int, input().split())) for _ in range(n)]
move_dir = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Please write your code here.
Dir = {1:(-1,0), 2: (-1,1), 3: (0,1), 4: (1,1), 5: (1,0), 6: (1,-1), 7: (0,-1), 8: (-1,-1)}
answer = 0

def is_range(x,y):
    return 0 <= x < n and 0 <= y < n

def simulate(row, col, cnt):
    global answer
    
    d = Dir[move_dir[row][col]]
    for s in range(n):
        dr, dc = s * d[0], s * d[1]
        nr = row + dr; nc = col + dc
        if not is_range(nr, nc):break

        if num[row][col] < num[nr][nc]:
            simulate(nr, nc, cnt + 1)
    
    answer = max(answer, cnt)

simulate(r - 1, c - 1, 0)
print(answer)


    
