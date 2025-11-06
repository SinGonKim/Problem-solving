from collections import defaultdict
n, m = map(int, input().split())

parents = [i for i in range(n+1)]
H = defaultdict(int)
for i in range(1,n+1):
    H[i] = 1

def find(x):
    if x == parents[x]:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a > b:
        a, b = b, a
    
    if a != b:
        H[a] += H[parents[b]]
        H[parents[b]] = 0
        parents[b] = a

for _ in range(m):
    op, *nums = input().split()
    if op == "x":
        a, b = map(int, nums)
        union(a,b)
    else:
        a = int(nums[0])
        root_a = find(a)
        print(H[root_a])

# Please write your code here.