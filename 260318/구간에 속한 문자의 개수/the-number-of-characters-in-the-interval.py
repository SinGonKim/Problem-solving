n, m, k = map(int, input().split())

# Read grid as list of strings since we need character-by-character access
grid = [input() for _ in range(n)]

# Read k queries as tuples
queries = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
mapping = {'a': 0, 'b': 1, 'c': 2}
board = [[[0]*3 for _ in range(m+1)] for _ in range(n+1)]
for i in range(n):
    for j in range(m):
        idx = mapping[grid[i][j]]
        for k in range(3):
            board[i+1][j+1][k] = board[i+1][j][k]
        board[i+1][j+1][idx] += 1

    
for query in queries:
    r1, c1, r2, c2 = query
    answer = [0, 0, 0]
    for i in range(r1, r2+1):
        for k in range(3):
            answer[k] += board[i][c2][k] - board[i][c1-1][k]
    print(*answer)
