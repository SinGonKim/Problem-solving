n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
from sortedcontainers import SortedSet
s = SortedSet(arr)
for i in range(len(s)-1,len(s)-k-1,-1):
    print(s[i], end = ' ')
