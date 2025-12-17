import sys
min_ = sys.maxsize
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
for i in range(n):
    min_x, min_y, max_x, max_y = sys.maxsize, sys.maxsize, -sys.maxsize, -sys.maxsize
    for j in range(n):
        if j == i:
            continue
        min_x = min(min_x, points[j][0])
        min_y = min(min_y, points[j][1])
        max_x = max(max_x, points[j][0])
        max_y = max(max_y, points[j][1])

    area = (max_x - min_x) * (max_y - min_y)
    min_ = min(min_, area)

print(min_)