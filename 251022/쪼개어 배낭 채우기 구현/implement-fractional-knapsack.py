N, M = map(int, input().split())
V = [tuple(map(int, input().split())) for _ in range(N)]
V.sort(key = lambda x: (x[1]/x[0]), reverse=True)


# Please write your code here.
target = 0
answer = 0
for v in V:
    if target + v[0] <= M:
        answer += v[1]
        target += v[0]
    elif v[0] != 0:
        answer += v[1]* (M-target)/v[0]
        break
    # print(answer, v[0], v[1])
print(f"{answer:.3f}")
