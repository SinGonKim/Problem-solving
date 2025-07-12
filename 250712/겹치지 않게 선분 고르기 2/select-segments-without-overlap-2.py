import sys
MIN_INT = -sys.maxsize -1
n = int(input())
a = [tuple(map(int, input().split())) for _ in range(n)]
a.sort(key=lambda x: (x[1],x[0]), reverse=True)

# Please write your code here.
dp = [1 for _ in range(n)]

def solution():
    n = len(a)

    for i in range(1, n):
        my_x, my_y = a[i]

        for j in range(0,i):
            before_x, before_y = a[j]

            if my_x == before_x or my_y == before_y:continue
            dp[i] = max(dp[j]+1, dp[i])
    return max(dp)
print(solution())