n = int(input())

# Please write your code here.
left = n
right = 2*n
while left <= right:
    mid = (left + right)//2
    x = mid//3
    y = mid//5
    z = mid//15
    if mid - (x + y - z) == n:
        while mid%3 == 0 or mid % 5 == 0:
            mid -= 1
        break
    elif mid - (x + y - z) > n:
        right = mid - 1
    else:
        left = mid + 1

print(mid)