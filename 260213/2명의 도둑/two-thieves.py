n, m, c = map(int, input().split())
weight = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
import heapq
heap = []
for i in range(n):
    for j in range(n):
        k = j+1
        w = weight[i][j]
        result = w**2
        while k<n and k - j < m:
            if w + weight[i][k] <= c:
                w += weight[i][k]
                result += weight[i][k]**2
                k += 1
            else:
                k -= 1
                break
        heapq.heappush(heap, (-result, i, j, k))

ans = 0
prev_row = -1
prev_col1 = -1
prev_col2 = -1
while heap:
    res, row, s, e = heapq.heappop(heap)
    if ans != 0:
        if prev_row == row and (prev_col1 <= s <= prev_col2 or s <= prev_col1 <= e):continue
        else:
            ans -= res
            break
    else:
        ans -= res
        prev_row = row
        prev_col1 = s
        prev_col2 = e
print(ans)
        