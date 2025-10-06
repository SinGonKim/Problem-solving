n, k = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(k)]

# arr[i] = 좌석 i에 앉은 사람 번호 (0-based)
arr = [i for i in range(n)]

# seats[사람번호] = 그 사람이 거쳐간 좌석들 (0-based)
seats = {}
for i in range(n):
    seats[i] = set()
    seats[i].add(i)

for _ in range(3):
    for edge in edges:
        a, b = edge[0] - 1, edge[1] - 1  # 1-based → 0-based 변환
        
        # 좌석 a와 좌석 b에 앉은 사람들을 교환
        arr[a], arr[b] = arr[b], arr[a]
        
        # 교환 후, 각 좌석에 앉은 사람에게 그 좌석 번호 기록
        seats[arr[a]].add(a)
        seats[arr[b]].add(b)

for i in range(n):
    print(len(seats[i]))