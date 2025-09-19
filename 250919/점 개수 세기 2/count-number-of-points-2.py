
import bisect
from collections import defaultdict

def main():
    n, q = map(int, input().split())
    
    # 점들을 y좌표별로 그룹화
    y_to_x = defaultdict(list)
    
    for _ in range(n):
        x, y = map(int, input().split())
        y_to_x[y].append(x)
    
    # 각 y좌표에서 x좌표들을 정렬 (이진탐색용)
    for y in y_to_x:
        y_to_x[y].sort()
    
    # y좌표들도 정렬
    sorted_y = sorted(y_to_x.keys())
    
    # 쿼리 처리
    for _ in range(q):
        x1, y1, x2, y2 = map(int, input().split())
        
        count = 0
        
        # y 범위에 있는 y좌표들을 이진탐색으로 찾기
        y_start = bisect.bisect_left(sorted_y, y1)
        y_end = bisect.bisect_right(sorted_y, y2)
        
        # 해당 y좌표들에서 x 범위에 있는 점들 계산
        for i in range(y_start, y_end):
            y = sorted_y[i]
            x_list = y_to_x[y]
            
            # x 범위에 있는 점들을 이진탐색으로 계산
            left_idx = bisect.bisect_left(x_list, x1)
            right_idx = bisect.bisect_right(x_list, x2)
            
            count += right_idx - left_idx
        
        print(count)
if __name__ == "__main__":
    main()