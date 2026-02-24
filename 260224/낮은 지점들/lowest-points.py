n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
d = dict()
for point in points:
    x, y = point
    if x in d and y >= d[x]:
        continue
    else:
        d[x] = y
answer = sum(d.values())
print(answer)