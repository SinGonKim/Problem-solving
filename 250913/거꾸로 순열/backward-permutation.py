n = int(input())

# Please write your code here.
from itertools import permutations

stack = [i for i in range(n,0,-1)]

for s in permutations(stack,n):
    print(*s)