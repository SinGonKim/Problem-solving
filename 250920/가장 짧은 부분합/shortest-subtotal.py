n, s = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
import sys
ans = sys.maxsize

sum_val = 0
j = 0
for i in range(n):
    while j<n and sum_val+arr[j] < s:
        sum_val += arr[j]
        j+= 1
    if j<n and sum_val+arr[j] >=s:
        ans = min(ans,j-i+1)
    sum_val -= arr[i]
if ans == sys.maxsize:
    print(-1)
else:
    print(ans)
