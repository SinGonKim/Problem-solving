n = int(input())

# Please write your code here.
from itertools import permutations
A = [i for i in range(1,n+1)]

for per in permutations(A):
    print(*per)