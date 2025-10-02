n, m = map(int, input().split())
arr = list(map(int, input().split()))
query = list(map(int, input().split()))

for q in query:
    left = 0
    right = n - 1
    result = -2
    
    # 올바른 방법 (최초 위치 찾기)
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= q:  # 같거나 크면
            if arr[mid] == q:
                result = mid
            right = mid - 1  # ✅ 계속 왼쪽 탐색
        else:
            left = mid + 1
    print(result+1)