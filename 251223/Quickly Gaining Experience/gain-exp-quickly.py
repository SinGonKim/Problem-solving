n, m = map(int, input().split())
quests = [tuple(map(int, input().split())) for _ in range(n)]

# 최대 시간: 퀘스트 수(100) * 최대 소요 시간(100) = 10,000
max_total_time = n * 100 
dp = [0] * (max_total_time + 1)

# 3. 0/1 배낭 문제 로직 (Bottom-Up DP)
# 각 퀘스트를 순회하며 가능한 최대 경험치 갱신
for exp, time in quests:
    # 중복 선택 방지를 위해 뒤에서부터 역순으로 계산
    for t in range(max_total_time, time - 1, -1):
        if dp[t - time] + exp > dp[t]:
            dp[t] = dp[t - time] + exp

# 4. 결과 출력
# 최소 시간부터 확인하며 경험치 M을 넘기는 순간 출력 후 종료
for t in range(max_total_time + 1):
    if dp[t] >= m:
        print(t)
        break
else:
    # 끝까지 M을 채우지 못한 경우
    print(-1)