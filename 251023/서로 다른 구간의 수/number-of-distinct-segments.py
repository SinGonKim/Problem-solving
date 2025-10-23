n = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
points = []
for i, (x1,x2) in enumerate(intervals):
    points.append((x1,+1,i))
    points.append((x2,-1,i))

points.sort()

segs = set()
ans = 0
for x, v, index in points:
    if v == +1:
        if not segs:
            ans += 1
        segs.add(index)
    else:
        segs.remove(index)

print(ans)
