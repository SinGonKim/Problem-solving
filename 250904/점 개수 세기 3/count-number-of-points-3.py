n, q = map(int, input().split())
points = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(q)]

# Please write your code here.
from sortedcontainers import SortedSet
import bisect
nums = SortedSet()

for v1, v2 in queries:
     # a 이상인 첫 인덱스
    left = bisect.bisect_left(points, v1)
    
    # b 이하인 마지막 인덱스 + 1
    right = bisect.bisect_right(points, v2)
    
    print(right - left)

    
