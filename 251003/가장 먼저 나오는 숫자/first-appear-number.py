n, m = map(int, input().split())
arr = list(map(int, input().split()))
querry = list(map(int, input().split()))

# Please write your code here.
import bisect
for q in querry:
    left = 0
    right = n-1
    while left <= right:
        if q < arr[left] or arr[right]<q:
            print(-1)
            break
        mid = (left+right)//2

        if q == arr[mid]:
            idx = bisect.bisect_left(arr,mid)
            print(idx+1)
            break
        
        elif q > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    else:
        print(-1)