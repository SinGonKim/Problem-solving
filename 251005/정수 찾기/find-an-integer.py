n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

# Please write your code here.
set1 = set(a)
for e in b:
    if e in set1:
        print(1)
    else:
        print(0)