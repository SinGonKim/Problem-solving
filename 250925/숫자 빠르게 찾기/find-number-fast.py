n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

# Please write your code here.
left = 0
right = n-1
for querry in queries:
    while left<=right:
        mid = (left+right)//2
        if arr[mid] < querry:
            left = mid + 1
        elif arr[mid] > querry:
            right = mid - 1
        else:
            print(mid+1)
            break
    else:
        print(-1)
    left = 0
    right = n - 1
