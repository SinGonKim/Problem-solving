import sys
INF = sys.maxsize
n = int(input())
k = int(input())

# Please write your code here.
start = 0
end = k
answer = 0

while start <= end:
    mid = (start + end)//2
    cnt = 0
    for i in range(1, n+1):
        cnt += min(mid//i, n)
    
    if cnt >= k:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1
print(answer)