n, m, k = map(int, input().split())

# Read grid as list of strings since we need character-by-character access
grid = [input() for _ in range(n)]

# Please write your code here.
mapping = {'a': 0, 'b': 1, 'c': 2}
board = [[[0]*2 for _ in range(m+1)] for _ in range(n+1)]
for i in range(n):
    for j in range(m):
        idx = mapping[grid[i][j]]
        for c in range(2):
            board[i+1][j+1][c] = board[i+1][j][c]
        if idx != 2:
            board[i+1][j+1][idx] += 1

    
for _ in range(k):
    r1, c1, r2, c2 = tuple(map(int, input().split()))
    answer = [0, 0, 0]
    for i in range(r1, r2+1):
        tmp = [0, 0]
        for c in range(2):
            tmp[c] = board[i][c2][c] - board[i][c1-1][c]
            answer[c] += tmp[c]
        answer[2] += c2 - c1 + 1 - sum(tmp[:2])
        
    print(*answer)
