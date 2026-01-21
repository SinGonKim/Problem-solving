MAX_INDEX = 4000001
n, k = map(int, input().split())
a = [0 for _ in range(MAX_INDEX)]
for _ in range(n):
    c, p = map(int, input().split())
    a[p] += c

ps = [0 for _ in range(MAX_INDEX)]
for i in range(MAX_INDEX):
    ps[i] = a[i]
    if i:
        ps[i] += ps[i-1]

ans = ps[2*k]
for i in range(k + 1, MAX_INDEX - k):
    ans = max(ans, ps[i + k] - ps[i - k - 1])

print(ans)