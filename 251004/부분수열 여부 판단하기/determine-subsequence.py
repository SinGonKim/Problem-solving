n, m = map(int, input().split())
A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))

# Please write your code here.

def is_subsequence():
    i = 1

    for j in range(1,m+1):
        while i <= n and A[i] != B[j]:
            i += 1

        if i == n+1:
            return False
        else:
            i += 1
    return True

if is_subsequence():
    print("Yes")
else:
    print("No")