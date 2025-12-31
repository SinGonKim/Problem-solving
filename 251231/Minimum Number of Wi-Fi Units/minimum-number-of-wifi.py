n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

cur = 0
cnt = 0
while cur < n:
    if arr[cur] == 0:
        cur += 1
        continue
    cur = min(cur + 2*m + 1, n)
    cnt += 1
    if cur != n and arr[cur] == 0:
        cur += 1
print(cnt)