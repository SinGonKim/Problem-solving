n, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))

# Please write your code here.

prefix_sum = [0 for _ in range(n+1)]

for i in range(1,n+1):
    prefix_sum[i] = prefix_sum[i-1] + arr[i]
ans = 0
nums = set(prefix_sum)
for num in nums:
    if num - k in nums:
        ans += 1
print(ans)
