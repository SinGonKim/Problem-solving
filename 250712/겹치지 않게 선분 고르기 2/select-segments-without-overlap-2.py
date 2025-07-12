import sys
MIN_INT = -sys.maxsize -1
n = int(input())
a = [tuple(map(int, input().split())) for _ in range(n)]
# a.sort(key=lambda x: (x[1],x[0]), reverse=True)
a.sort(key=lambda x: x[1])

# Please write your code here.


def solution():
    cnt = 0
    last_end = -1

    for s, e in a:
        if s > last_end:
            cnt += 1
            last_end = e
    return cnt


print(solution())