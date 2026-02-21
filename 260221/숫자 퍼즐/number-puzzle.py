import sys
from functools import lru_cache


INF = sys.maxsize # cap counts to avoid big integers (K <= 1e9)

@lru_cache(None)
def count(pos: int, prev: int, rem: int) -> int:
    """Number of nondecreasing sequences a[pos..n-1] with a[pos] >= prev and sum = rem."""
    if pos == n:
        return 1 if rem == 0 else 0

    length = n - pos
    # 최소합: 모두 prev로 채움
    if rem < prev * length:
        return 0

    maxx = rem // length  # because rem >= x * length must hold
    total = 0
    for x in range(prev, maxx + 1):
        total += count(pos + 1, x, rem - x)
        if total >= INF:
            return INF
    return total

if __name__ == "__main__":

    n, m, k = map(int, sys.stdin.readline().split())
    ans = []
    prev = 1
    rem = m

    for pos in range(n): # position 0 ~ n - 1
        length = n - pos # 뒤에 남은 길이
        maxx = rem // length # max

        for x in range(prev, maxx + 1):
            c = count(pos + 1, x, rem - x)

            if k > c:
                k -= c
            else:
                ans.append(x)
                prev = x
                rem -= x
                break

    print(*ans)
