import sys
import math
input = sys.stdin.readline
n = int(input())
T =list(int(input()) for _ in range(n))
T.sort()
interval = list()
ans = list()
for i in range(1, n):
    interval.append(T[i] - T[i-1])
prev = interval[0]
for i in range(1, len(interval)):
    prev = math.gcd(prev, interval[i]) #숫자간의 차이의 최대공약수를 이용하여 주어진 수의 최대공약수를 구하려한다.
for i in range(2, int(math.sqrt(prev))+1):
    if prev% i ==0:
        ans.append(i)
        ans.append(prev//i)
ans.append(prev)
ans = list(set(ans))
ans.sort()
print(*ans)
