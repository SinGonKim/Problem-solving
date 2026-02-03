import sys
sys.setrecursionlimit(10*6)
s = input()
t = input()

# Please write your code here.
len_s = len(s)
len_t = len(t)

dp = [[len_s + len_t for _ in range(len_t + 1)] for _ in range(len_s+1)]

def recursive(s_n, t_n):
    global dp
    ls = len(s_n)
    lt = len(t_n)
    if ls == 0 or lt == 0:
        dp[0][0] = min(dp[0][0], dp[ls][lt] + ls + lt)
        return
    
    if s_n[-1] == t_n[-1]:
        dp[ls-1][lt-1] = min(dp[ls-1][lt-1], dp[ls][lt] + 1)
        recursive(s_n[:-1], t_n[:-1])
    else:
        dp[ls-1][lt] = min(dp[ls-1][lt], dp[ls][lt] + 1)
        recursive(s_n[:-1], t_n)
        dp[ls][lt-1] = min(dp[ls][lt-1], dp[ls][lt] + 1)
        recursive(s_n, t_n[:-1])

dp[len_s][len_t] = 0
recursive(s,t)
print(dp[0][0])
