n = int(input())
m = []
groups = []

for _ in range(n):
    nums = list(map(int, input().split()))
    m.append(nums.pop(0))
    res = 0
    for num in nums:
        res |= 1<<num
    groups.append(res)

# Please write your code here.
answer = 0
from itertools import combinations

for (a, b) in combinations(groups, 2):
    if a & b == 0:
        answer += 1
print(answer)