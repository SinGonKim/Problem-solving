n = int(input())
arr = list(map(int, input().split()))


# 왼쪽에서 각 위치까지의 최대값과 인덱스 저장
left_max = [-float('inf')] * n
left_idx = [-1] * n

max_val = arr[0]
max_pos = 0

for i in range(2, n):
    left_max[i] = max_val
    left_idx[i] = max_pos
    if arr[i - 1] > max_val:
        max_val = arr[i - 1]
        max_pos = i - 1

# 오른쪽에서 각 위치까지의 최대값과 인덱스 저장
right_max = [-float('inf')] * n
right_idx = [-1] * n

max_val = arr[n - 1]
max_pos = n - 1

for i in range(n - 3, -1, -1):
    right_max[i] = max_val
    right_idx[i] = max_pos
    if arr[i + 1] > max_val:
        max_val = arr[i + 1]
        max_pos = i + 1

# 중간 값을 기준으로 최대 합 계산
max_sum = -float('inf')
result_indices = []

for mid in range(2, n - 2):
    current_sum = left_max[mid] + arr[mid] + right_max[mid]
    if current_sum > max_sum:
        max_sum = current_sum
        result_indices = [left_idx[mid], mid, right_idx[mid]]

print(max_sum)