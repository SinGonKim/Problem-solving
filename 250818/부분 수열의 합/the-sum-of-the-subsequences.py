n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
dp = [-1 for _ in range(m+1)]
dp[0] = 1
stack = set()
stack.add(0)
for i in range(n):
    tmp = []
    for j in stack:
        if j + A[i] <= m:
            dp[j+A[i]] = 1
            tmp.append(j+A[i])
    for t in tmp:
        stack.add(t)


if dp[m] == 1:
    print('Yes')
else:
    print('No')
