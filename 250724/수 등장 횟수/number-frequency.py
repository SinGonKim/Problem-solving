n, m = map(int, input().split())
arr = list(map(int, input().split()))
nums = list(map(int, input().split()))

# Please write your code here.
from collections import defaultdict
answer = defaultdict(list)

for i, num in enumerate(arr):
    answer[num].append(i)
for num in nums:
    print(len(answer[num]), end = ' ')