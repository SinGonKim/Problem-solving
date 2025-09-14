n, k = map(int, input().split())
arr = sorted(list(map(int, input().split())))

# Please write your code here.
left = 0
right = n-1
ans = 0
while left<right:
    if arr[left] + arr[right] == k:
        ans += 1
        if arr[left+1] - arr[left] <= arr[right]- arr[right-1]:
            left += 1
        else:
            right -= 1
    
    elif arr[left] + arr[right] > k:
        right -= 1
    else:
        left += 1
print(ans)