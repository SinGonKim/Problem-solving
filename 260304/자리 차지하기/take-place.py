n, m = map(int, input().split())
a = list(map(int, input().split()))

# Please write your code here.
seats = [False for _ in range(m+1)]

for ai in a:
    for s in range(ai, 0, -1):
        if not seats[s]:
            seats[s] = True
            break
    else:break
print(sum(seats))