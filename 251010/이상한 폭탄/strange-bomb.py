n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

R = [0 for _ in range(n)]

latest_index = dict()
for i in range(n-1,-1,-1):
    if arr[i] not in latest_index:
        R[i] = -1
    else:
        R[i] = latest_index[arr[i]]
    latest_index[arr[i]] = i

answer = -1
for i in range(n):
    if R[i] != -1 and R[i] - i <= k:
        answer = max(answer, arr[i])
print(answer)