n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
from collections import defaultdict
d = defaultdict(int)
ans = 0
for i in range(n):
    for j in range(i+1,n):
        arr1 = arr[i]; arr2 = arr[j]
        res = k - arr1 - arr2

        if res in d:
            ans += d[res]
    
    
    d[arr1] += 1
print(ans)



