from collections import deque


def can_reach(d):
    min_val = min(map(min, grid))
    max_val = max(map(max, grid))

    for low in range(min_val, max_val - d + 1):
        high = low + d
        if grid[0][0] < low or grid[0][0] > high: continue

        visited = [[False for _ in range(n)] for _ in range(n)]
        queue = deque()
        queue.append((0,0))
        visited[0][0] = True

        while queue:
            x, y = queue.popleft()
            if x == n-1 and y == n-1:
                return True
            
            for dx, dy in [(1,0), (0,1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0<=ny<n and not visited[nx][ny]:
                    if low <= grid[nx][ny] <= high:
                        visited[nx][ny] = True
                        queue.append((nx,ny))
    return False



def simulate():
    left, right = 0, max(map(max, grid)) - min(map(min,grid))
    answer = right

    while left <= right:
        mid = (left + right)//2
        if can_reach(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return answer


# Please write your code here.
if __name__ == "__main__":
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    ans = simulate()
    print(ans)