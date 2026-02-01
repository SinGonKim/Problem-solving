n = int(input())
L = []

for _ in range(n):
    a, b = map(int, input().split())
    L.append((a,b))

# Please write your code here.
L = sorted(L, key = lambda x: (x[1], x[0]))
dp = [0 for _ in range(n+1)]
stack = []

for idx, (s, e) in enumerate(L,1):
    if not len(stack):
        stack.append((s, e))
    else:
        prev_s, prev_e = stack[-1]
        if prev_e < s:
            stack.append((s,e))
    dp[idx] = len(stack)
print(dp[n])

