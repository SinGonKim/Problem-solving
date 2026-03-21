n = int(input())

# Please write your code here.
if n < 5 and n % 2 != 0:
    print(-1)
else:
    ans = 0
    L = n//5
    res = n%5
    if res%2 and L > 0:
        res += 5
        L -= 1
    res = (n - L*5)//2
    print(L + res)