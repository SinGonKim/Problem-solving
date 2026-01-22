direction = [(1,0), (0,1), (0,-1), (-1,0)]
dire_dict = {"U": 3, "L": 2, "R": 1, "D": 0}

n, m, t, k = map(int, input().split())

marble = []
for i in range(1, m+1):
    r, c, d, v = input().split()
    d = dire_dict[d]
    r, c, v = int(r) - 1, int(c) - 1, int(v)
    marble.append((i, r, c, d, v))

marble.sort(key=lambda x: (x[4], x[0]), reverse=True)

def check_range(r, c):
    return 0 <= r < n and 0 <= c < n
 
grid = [[0] * (n) for _ in range(n)]

for _ in range(t):
    new_grid = [[0] * (n) for _ in range(n)]
    new_marble = []

    for target in marble:
        idx, r, c, d, v = target

        for _ in range(v):
            nx, ny = r + direction[d][0], c + direction[d][1]
            
            if check_range(nx, ny):
                r, c = nx, ny
            else:
                d = (3 - d) % 4
                nx, ny = r + direction[d][0], c + direction[d][1]
                r, c = nx, ny
        
        if new_grid[r][c] < k:
            new_grid[r][c] += 1
            new_marble.append((idx, r, c, d, v))

    marble = sorted(new_marble, key=lambda x: (x[4], x[0]), reverse=True)
    grid = new_grid

print(len(marble))

