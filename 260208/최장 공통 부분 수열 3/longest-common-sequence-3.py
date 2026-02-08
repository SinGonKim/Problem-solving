n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
# dp[i]는 b[i]를 마지막 원소로 하는 LCS의 정보를 담습니다.
# dp[i] = [길이, [수열 리스트]]
dp = [[0, []] for _ in range(m)]

for i in range(n):
    current_val = a[i]
    if current_val not in b: continue

    target_idx = b.index(current_val)

    best_len = 0
    best_seq = []


    for j in range(target_idx):
        if dp[j][0] > best_len:
            best_len = dp[j][0]
            best_seq = dp[j][1]
        elif dp[j][0] == best_len and best_len > 0:
            # 길이는 같은데 사전순으로 더 앞서는 수열이 있다면 교체
            if dp[j][1] < best_seq:
                best_seq = dp[j][1]
    # 현재 원소를 추가하여 갱신
    dp[target_idx] = [best_len + 1, best_seq + [current_val]]

# 전체 dp 테이블에서 가장 긴 수열들을 찾고, 그중 사전순으로 가장 앞선 것 선택
max_len = 0
for length, seq in dp:
    if length > max_len:
        max_len = length
        
candidates = [seq for length, seq in dp if length == max_len]
candidates.sort() # 사전순 정렬

if not candidates:
    # 공통 부분 수열이 없는 경우 (문제 조건상 최소 1개는 존재할 가능성이 높음)
    print()
else:
    # 결과 출력
    result = candidates[0]
    print(*(result))