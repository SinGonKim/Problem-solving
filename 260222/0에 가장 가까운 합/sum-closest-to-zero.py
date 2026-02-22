import sys
n = int(input())
a = sorted(list(map(int, input().split())))

# Please write your code here.
left = 0
right = n-1
answer = sys.maxsize
while left < right:
    answer = min(answer ,abs(a[left] + a[right]))
    if a[left] + a[right] >= 0:
        right -= 1
    else:
        left += 1
print(answer)
        