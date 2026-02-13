n, m, c = map(int, input().split())
weight = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
import heapq

def solve_max_square_sum(nums, C):
    # dp[w]는 원소들의 합이 w일 때 얻을 수 있는 '최대 제곱합'
    # 초기값 -1은 해당 합계를 만들 수 없음을 의미
    dp = [-1] * (C + 1)
    dp[0] = 0
    
    # 경로 추적을 위해 (이전 합계, 사용된 원소의 인덱스) 저장
    parent = [None] * (C + 1)

    for idx, num in enumerate(nums):
        num_sq = num ** 2
        # 역순 순회하여 자기 자신 중복 선택 방지
        for w in range(C, num - 1, -1):
            if dp[w - num] != -1:
                # 현재 저장된 값보다 '이 숫자를 추가했을 때의 제곱합'이 더 크면 갱신
                if dp[w - num] + num_sq > dp[w]:
                    dp[w] = dp[w - num] + num_sq
                    parent[w] = (w - num, idx)

    # 전체 dp 테이블에서 가장 큰 제곱합(Value)과 그때의 합계(Weight) 찾기
    max_sq_val = -1
    best_w = 0
    for w in range(C + 1):
        if dp[w] > max_sq_val:
            max_sq_val = dp[w]
            best_w = w

    # 역추적하여 어떤 숫자들이 선택되었는지 리스트업
    selected_elements = []
    curr_w = best_w
    while curr_w > 0 and parent[curr_w] is not None:
        prev_w, idx = parent[curr_w]
        selected_elements.append(nums[idx])
        curr_w = prev_w

    return max_sq_val, best_w, selected_elements

heap = []
for i in range(n):
    for j in range(n):
        candidates = weight[i][j:min(j+m,n)]
        max_sq, total_sum, elements = solve_max_square_sum(candidates, c)
        heapq.heappush(heap, (-max_sq, i, j, min(j+m,n)))

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
        
