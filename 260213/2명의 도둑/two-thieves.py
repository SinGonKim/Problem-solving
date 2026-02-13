import sys

def solve():
    n, m, c = map(int, sys.stdin.readline().split())
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    # 특정 구간(nums)에서 합이 C 이하가 되도록 선택했을 때의 최대 제곱합 계산 (DP)
    def get_max_val(nums):
        dp = [0] * (c + 1)
        for num in nums:
            for w in range(c, num - 1, -1):
                dp[w] = max(dp[w], dp[w - num] + num * num)
        return max(dp)

    # 1. 모든 가능한 구간의 최대 가치를 미리 계산하여 저장
    # info list: (행 번호, 시작 열, 끝 열, 최대 가치)
    possible_areas = []
    for i in range(n):
        for j in range(n - m + 1):
            subset = grid[i][j:j + m]
            max_val = get_max_val(subset)
            possible_areas.append((i, j, j + m - 1, max_val))

    ans = 0
    size = len(possible_areas)

    # 2. 두 도둑이 선택할 수 있는 모든 조합 탐색
    for i in range(size):
        for j in range(i + 1, size):
            r1, s1, e1, v1 = possible_areas[i]
            r2, s2, e2, v2 = possible_areas[j]

            # 같은 행일 경우 영역이 겹치는지 확인
            if r1 == r2:
                if not (e1 < s2 or e2 < s1):
                    continue
            
            # 겹치지 않는다면 최댓값 갱신
            ans = max(ans, v1 + v2)

    print(ans)

solve()