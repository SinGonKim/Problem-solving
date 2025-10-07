s = int(input())

# Please write your code here.
left = 0
right = s
max_num = 0

while left <= right:
    mid = (left+right)//2
    if mid*(mid+1)//2 <= s:
        left = mid + 1
        max_num = max(max_num, mid)
    else:
        right = mid - 1
print(max_num)