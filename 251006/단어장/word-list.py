n = int(input())
words = [input() for _ in range(n)]

# Please write your code here.
from sortedcontainers import SortedDict

sd = SortedDict()
for word in words:
    if not word in sd:
        sd[word] = 1
    else:
        sd[word] += 1
for k, v in sd.items():
    print(k, v)