from functools import cmp_to_key

def compare(x, y):
    if x + y > y + x:
        return -1
    elif x + y == y + x:
        return 0
    else:
        return 1

n = int(input())
arr = sorted([input() for _ in range(n)], key = cmp_to_key(compare))

# Please write your code here.
answer = "".join(arr)
print(answer)
