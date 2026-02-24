string = list(input().strip())


# Please write your code here.
from collections import defaultdict

d = defaultdict(int)
for s in string:
    d[s] += 1

L = [k for k, v in d.items() if v == 1]
if len(L):
    print(L[0])
else:
    print("None")
