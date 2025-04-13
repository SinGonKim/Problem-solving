n = int(input())
num = list(map(int, input().split()))
max_L, max_R = map(int, input().split())

cnt = 0
for m in num:
    m -= max_L
    cnt += 1
    if m > 0:
        b = m%max_R
        a = m//max_R
        if b>0:
            cnt += a + 1
        else:
            cnt += a
print(cnt)