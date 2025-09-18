N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = list(w), list(v)

# Please write your code here.
dp = [0 for _ in range(M+1)]

stack = set()
for i in range(N):
    w_i, v_i = w[i], v[i]
    if w_i <= M:
        dp[w_i] = max(dp[w_i], v_i)
    S = sorted(list(stack), reverse=True)
    for s in S:
        if s + w_i <= M:
            stack.add(s+w_i)
            dp[s+w_i] = max(dp[s+w_i], dp[s]+v_i)
    stack.add(w_i)
print(max(dp))
