import sys

# 재귀 깊이 제한 해제
sys.setrecursionlimit(200000)

def solve():
    # dp[remainder][has_369]: prefix가 N보다 작은 경우의 수
    # remainder: 0, 1, 2 / has_369: 0 (없음), 1 (있음)
    dp = [[0, 0] for _ in range(3)] # 3으로 나눴을 때 나머지 * 3,6,9 유무
    
    # N과 똑같이 따라가고 있는 상태 (tight path)
    tight_rem = 0
    tight_has = 0
    
    for char in s_n:
        limit = ord(char) - ord('0')
        next_dp = [[0, 0] for _ in range(3)]
        
        # 1. 기존 dp 상태에서 확장 (이미 N보다 작아진 숫자들)
        for r in range(3):
            # 이미 3, 6, 9가 포함된 경우 (has_369 == 1)
            if dp[r][1]:
                val = dp[r][1]
                # 어떤 숫자가 와도 has_369는 1로 유지
                next_dp[r][1] = (next_dp[r][1] + val * 4) % MOD           # d % 3 == 0 (0,3,6,9)
                next_dp[(r + 1) % 3][1] = (next_dp[(r + 1) % 3][1] + val * 3) % MOD # d % 3 == 1 (1,4,7)
                next_dp[(r + 2) % 3][1] = (next_dp[(r + 2) % 3][1] + val * 3) % MOD # d % 3 == 2 (2,5,8)
            
            # 3, 6, 9가 아직 포함되지 않은 경우 (has_369 == 0)
            if dp[r][0]:
                val = dp[r][0]
                next_dp[r][0] = (next_dp[r][0] + val) % MOD              # d == 0
                next_dp[(r + 1) % 3][0] = (next_dp[(r + 1) % 3][0] + val * 3) % MOD # d == 1, 4, 7
                next_dp[(r + 2) % 3][0] = (next_dp[(r + 2) % 3][0] + val * 3) % MOD # d == 2, 5, 8
                next_dp[r][1] = (next_dp[r][1] + val * 3) % MOD           # d == 3, 6, 9 (rem 0, has 1)

        # 2. tight path에서 확장 (현재 자릿수에서 N보다 작아지는 경우)
        for d in range(limit):
            nr = (tight_rem * 10 + d) % 3
            nh = 1 if (tight_has or d in (3, 6, 9)) else 0
            next_dp[nr][nh] = (next_dp[nr][nh] + 1) % MOD
        
        # 3. tight path 업데이트 (N과 동일한 경로 유지)
        tight_rem = (tight_rem * 10 + limit) % 3
        tight_has = 1 if (tight_has or limit in (3, 6, 9)) else 0
        
        dp = next_dp

    # 결과 취합: 3의 배수(r==0)이거나 3,6,9 포함(h==1)인 경우
    ans = 0
    for r in range(3):
        for h in range(2):
            if r == 0 or h == 1:
                ans = (ans + dp[r][h]) % MOD
    
    # 마지막 tight path(숫자 N 그 자체) 확인
    if tight_rem == 0 or tight_has == 1:
        ans = (ans + 1) % MOD
        
    # '0'은 3의 배수이지만 게임 범위(1~N)가 아니므로 1을 뺌
    print((ans - 1 + MOD) % MOD)


if __name__ == "__main__":
    s_n = input().strip() 
    N_len = len(s_n)
    MOD = 10**9 + 7
    solve()