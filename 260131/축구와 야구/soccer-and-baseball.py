n = int(input())
players = []
for _ in range(n):
    si, bi = map(int, input().split())
    players.append((si,bi))

# Please write your code here.
dp = [[-1] * 10 for _ in range(12)]
dp[0][0] = 0

for s_ability, b_ability in players:
    # 중복 선택을 방지하기 위해 역순으로 순회 (1/0 배낭 문제 방식)
    for s in range(11, -1, -1):
        for b in range(9, -1, -1):
            if dp[s][b] == -1:
                continue
            
            # 1. 현재 학생을 축구팀에 넣는 경우
            if s + 1 <= 11:
                dp[s+1][b] = max(dp[s+1][b], dp[s][b] + s_ability)
            
            # 2. 현재 학생을 야구팀에 넣는 경우
            if b + 1 <= 9:
                dp[s][b+1] = max(dp[s][b+1], dp[s][b] + b_ability)
            
            # 3. 현재 학생을 뽑지 않는 경우: dp[s][b] 값 유지 (코드상 구현 불필요)

print(dp[11][9])