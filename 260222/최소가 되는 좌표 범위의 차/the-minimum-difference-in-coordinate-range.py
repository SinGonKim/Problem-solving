n, d = map(int, input().split())
points = sorted([tuple(map(int, input().split())) for _ in range(n)], key = lambda x: (x[1], x[0]))

# Please write your code here.
left = 0
right = 1
import sys
answer = sys.maxsize

while right < n:
    if points[right][1] - points[left][1] < d:
        right += 1
        continue
    answer = min(answer, abs(points[right][0] - points[left][0]))
    if right == n-1:
        left += 1
        right = left + 1
    else:
        right += 1
if answer == sys.maxsize:
    print(-1)
else:
    print(answer)