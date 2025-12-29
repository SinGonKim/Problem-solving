n = int(input())
blocks = [int(input()) for _ in range(n)]

# Please write your code here.
mean = sum(blocks)//len(blocks)

cnt = 0
for block in blocks:
    diff = abs(block-mean)
    cnt += diff
print(cnt//2)