n, m = map(int, input().split())
points = sorted(list(map(int, input().split())))
segments = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

def find(t):
    left = 0
    right = len(points) - 1
    min_idx = n

    while left <= right:
        mid = (left+right)//2
        if points[mid] >= t:
            min_idx = min(min_idx, mid)
            right = mid - 1
        else:
            left = mid + 1
    return min_idx



for a, b in segments:
    end = find(b)
    start = find(a)
    ans = end - start
    if end < n and points[end] == b:
        ans += 1
    print(ans)