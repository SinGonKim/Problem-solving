
# N: 보석 종류의 수, M: 가방의 최대 무게
N, M = map(int, input().split())

# 보석 정보를 저장할 리스트
jewels = list(tuple(map(int, input().split())) for _ in range(N))

# dp 배열 초기화: dp[j]는 무게가 j일 때의 최대 가치를 저장
# 인덱스를 무게와 일치시키기 위해 크기를 M+1로 설정하고 0으로 초기화
dp = [0] * (M + 1)

# 동적 프로그래밍을 이용한 최대 가치 계산
# 1부터 M까지 모든 무게에 대해 최대 가치를 계산
for current_weight in range(1, M + 1):
    # 각 보석을 하나씩 확인
    for w, v in jewels:
        # 현재 무게(current_weight)에 해당 보석(w)을 담을 수 있는 경우
        if current_weight >= w:
            # 기존의 최대 가치와, 
            # (현재 무게 - 보석 무게)일 때의 최대 가치 + 현재 보석의 가치를 비교하여 더 큰 값을 저장
            dp[current_weight] = max(dp[current_weight], dp[current_weight - w] + v)

# 최종적으로 무게 M일 때의 최대 가치를 출력
print(dp[M])