N = int(input())

# Please write your code here.
from collections import deque

def bfs(n):
    que = deque()
    if n == 1:
        return 0
    visited = [-1 for _ in range(2*n+2)]
    que.append((n,0))
    visited[n] = 0

    while que:
        x, c = que.popleft()

        if x == 1:
            return c

        if x-1>0 and visited[x-1] == -1:
            que.append((x-1,c+1))
            visited[x-1] = visited[x] + 1
        
        if x+1<=2*n and visited[x+1] == -1:
            que.append((x+1,c+1))
        
        if x%2 == 0 and visited[x//2] == -1:
            que.append((x//2, c+1))
        
        if x%3 == 0 and visited[x//3] == -1:
            que.append((x//3,c+1))


answer = bfs(N)
print(answer)