
n, m = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

# Please write your code here.
resultA = A - B
resultB = B - A
answer = len(resultA.union(resultB))
print(answer)