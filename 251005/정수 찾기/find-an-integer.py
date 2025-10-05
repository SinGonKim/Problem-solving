n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

# Please write your code here.
for i in range(m):
    if b[i] in set(a):
        print(1)
    else:
        print(0)