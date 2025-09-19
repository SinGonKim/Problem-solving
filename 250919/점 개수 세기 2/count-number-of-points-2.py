
import bisect
from collections import defaultdict

def main():
    n, q = map(int, input().split())
    
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    
    # x좌표로 정렬
    points.sort()
    
    for _ in range(q):
        x1, y1, x2, y2 = map(int, input().split())
        
        count = 0
        
        # x 범위를 이진탐색으로 좁힌 후, y만 체크
        left_bound = bisect.bisect_left(points, (x1, float('-inf')))
        right_bound = bisect.bisect_right(points, (x2, float('inf')))
        
        # x 범위 내의 점들에서 y 범위 체크
        for i in range(left_bound, right_bound):
            _, y = points[i]
            if y1 <= y <= y2:
                count += 1
        
        print(count)
if __name__ == "__main__":
    main()