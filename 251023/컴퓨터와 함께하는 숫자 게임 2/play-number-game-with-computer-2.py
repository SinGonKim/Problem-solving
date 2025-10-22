m = int(input())
a, b = map(int, input().split())

# Please write your code here.
C = [0 for _ in range(m+1)]

for i in range(a,b+1):
    if C[i] == 0:
        left = 1
        right = m
        cnt = 0
        while left <= right:
            cnt += 1
            mid = (left+right)//2
            if C[mid] == 0:
                C[mid] = cnt
            if mid < i:
                left = mid + 1
            elif mid >i :
                right = mid - 1
            else:
                break

MIN = min(C[a:b+1])
MAX = max(C[a:b+1])
# print(C)
print(MIN, MAX)