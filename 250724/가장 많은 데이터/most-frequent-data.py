n = int(input())
words = [input() for _ in range(n)]

# Please write your code here.
from collections import Counter
c = Counter(words)
print(max(c.values()))