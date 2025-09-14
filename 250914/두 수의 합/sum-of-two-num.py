n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
from collections import Counter
C = Counter(arr)
arr = sorted(list(set(arr)))
left = 0
right = len(arr)-1
ans = 0
while left<right:
    if arr[left] + arr[right] == k:
        ans += C[arr[left]]*C[arr[right]]
        left += 1
    elif arr[left] + arr[right] > k:
        right -= 1
    else:
        left += 1

for key, value in C.items():
    if 2*key == k:
        ans += (value*(value-1))//2
print(ans)