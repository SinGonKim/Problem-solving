

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

# Please write your code here.
def is_range(x,y):
    if 1<=x<=n and 1<=y<=n:
        return True
    return False


from collections import deque
def bfs():
    que = deque()
    visited = [[-1 for _ in range(n+1)] for _ in range(n+1)]

    visited[r1][c1] = 0
    que.append((r1,c1,0))

    dxs = [-2,-1,1,2,-2,-1,1,2]
    dys = [-1,-2,-2,-1,1,2,2,1]
    while que:
        r, c, num = que.popleft()
        if r == r2 and c == c2:
            return num

        for dx, dy in zip(dxs, dys):
            nx = r + dx; ny = c + dy


            if is_range(nx,ny) and visited[nx][ny] == -1:
                que.append((nx,ny,num+1))
                visited[nx][ny] = visited[r][c]+1
    return -1
ans = bfs()
print(ans)