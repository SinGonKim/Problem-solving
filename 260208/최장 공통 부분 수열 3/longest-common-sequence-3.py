n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
dp = [[0,[]] for _ in range(m)]

for i in range(n):
    current_val = a[i]
    if current_val not in b: continue

    target_index = b.index(current_val)
    best_len = 0
    best_seq = []

    for j in range(target_index):
        if dp[j][0] > best_len:
            best_len = dp[j][0]
            best_seq = dp[j][1]
        elif dp[j][0] == best_len and best_len > 0:
            if best_seq > dp[j][1]:
                best_seq = dp[j][1]
    dp[target_index] = [best_len + 1, best_seq + [current_val]]

max_len = 0

for l, seq in dp:
    if max_len < l:
        max_len = l

candidate = [seq for l, seq in dp if l == max_len]
candidate.sort()

print(*candidate[0])