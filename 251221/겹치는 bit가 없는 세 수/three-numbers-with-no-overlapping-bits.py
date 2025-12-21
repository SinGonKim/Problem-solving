from itertools import combinations
n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

if len(arr)<3:
    print(0)
else:
    answer = 0
    for comb in combinations(arr,3):
        if sum(comb) == (comb[0]|comb[1]|comb[2]):
            answer = max(answer, sum(comb))
    print(answer)
