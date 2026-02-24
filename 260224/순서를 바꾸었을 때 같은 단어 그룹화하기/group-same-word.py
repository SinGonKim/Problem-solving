n = int(input())
words = [input() for _ in range(n)]

# Please write your code here.
from collections import defaultdict
d = defaultdict(int)

for word in words:
    s = "".join(sorted(word))
    d[s] += 1

answer = max(d, key = d.get)
print(d[answer])