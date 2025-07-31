n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
S = sum(arr[:k])
target = S
for i in range(k,n):
    S += +arr[i]-arr[i-k]
    if S > target:
        target = S
print(target)