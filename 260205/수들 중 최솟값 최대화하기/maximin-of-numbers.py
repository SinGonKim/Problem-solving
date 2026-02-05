import sys
INF = sys.maxsize
sys.setrecursionlimit(10*6)
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
answer = 0
# Please write your code here.

def solution(row, visited, cnt):
    global answer
    if row == n:
        answer = max(answer, cnt)
        return

    for col in range(n):
        if visited[col]: continue
        visited[col] = 1
        solution(row+1, visited, min(cnt, grid[row][col]))
        visited[col] = 0

visit = [0 for _ in range(n)]
solution(0, visit, INF)
print(answer)