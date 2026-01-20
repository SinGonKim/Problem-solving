n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
ans = 0
current_sum = 0
start = 0

for end in range(n):
    current_sum += arr[end]

    while current_sum > m:
        current_sum -= arr[start]
        start += 1
    
    if current_sum == m:
        ans += 1

print(ans)