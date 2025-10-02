n, m = map(int, input().split())
arr = list(map(int, input().split()))
query = list(map(int, input().split()))

for q in query:
    left = 0
    right = n - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == q:
            result = mid + 1  # 1-based index
            right = mid - 1   # 최초 위치를 찾기 위해 왼쪽 계속 탐색
        elif arr[mid] < q:
            left = mid + 1
        else:
            right = mid - 1
    
    print(result)