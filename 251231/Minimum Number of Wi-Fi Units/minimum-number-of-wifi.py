n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

cur = -1
cnt = 0
for i in range(n):
    if i - m <= cur or arr[i-m] == 0: continue
    cur = i + m
    cnt += 1
    if cur >= n-1:break
else:
    for k in range(cur+1,n):
        if arr[k]:
            cnt += 1
            break
    else:
        cnt = 1
print(cnt)