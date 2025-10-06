n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
from sortedcontainers import SortedDict
sd = SortedDict()

for idx, x in enumerate(arr,1 ):
    if not x in sd:
        sd[x] = idx

for k, v in sd.items():
    print(k, v)