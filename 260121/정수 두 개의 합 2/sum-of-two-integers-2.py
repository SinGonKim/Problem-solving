from bisect import bisect_right
n, k = map(int, input().split())
arr = sorted([int(input()) for _ in range(n)])

# Please write your code here.
ans = 0
for left_idx, num in enumerate(arr):
    if num >= k: break
    res = k - num
    right_idx = bisect_right(arr, res)
    if right_idx - left_idx <= 1:break
    ans += right_idx - left_idx -1
print(ans)
