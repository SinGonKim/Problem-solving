import sys
INF = sys.maxsize
n, m = map(int, input().split())
arr = sorted([int(input()) for _ in range(m)])

# Please write your code here.
left = 0
right = arr[-1]*n
answer = INF

while left <= right:
    mid = (left + right)//2
    result = 0
    for num in arr:
        result += mid//num
    if result >= n:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)