n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

cur = -1
cnt = 0
for i in range(n):
    if i - m <= cur or arr[i-m] == 0: continue
    cur = i + m
    cnt += 1
    if cur >= n:break
print(cnt)