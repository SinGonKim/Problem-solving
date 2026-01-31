import sys

# 재귀 깊이 제한 해제
sys.setrecursionlimit(200000)

def dp(idx, is_limit, remainder, has_369):
    # memoization: [index][is_limit][remainder][has_369]
    memo = {}
    # 기저 사례: 모든 자릿수를 결정했을 때
    if idx == N_len:
        # 3, 6, 9가 포함되어 있거나 3의 배수인 경우 1 반환
        return 1 if (has_369 or remainder == 0) else 0
    
    state = (idx, is_limit, remainder, has_369)
    if state in memo:
        return memo[state]
    
    res = 0
    # 현재 자릿수에서 쓸 수 있는 최대 숫자 결정
    upper = int(s_n[idx]) if is_limit else 9
    
    for digit in range(upper + 1):
        new_is_limit = is_limit and (digit == upper)
        new_has_369 = has_369 or (digit in [3, 6, 9])
        new_remainder = (remainder * 10 + digit) % 3
        
        res = (res + dp(idx + 1, new_is_limit, new_remainder, new_has_369)) % MOD
        
    memo[state] = res
    return res

def solve():
    # 1부터 시작하므로 0인 경우(결과가 1로 나옴)를 하나 빼줍니다.
    # dp 함수는 0부터 N까지의 조건을 만족하는 수의 개수를 구합니다.
    ans = (dp(0, True, 0, False) - 1 + MOD) % MOD
    print(ans)

if __name__ == "__main__":
    s_n = input().strip() 
    N_len = len(s_n)
    MOD = 10**9 + 7
    solve()