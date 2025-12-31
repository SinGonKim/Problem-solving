n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.
if n == 1:
    print(0)
else:
    answer = 0
    for i in range(n-1,0,-1):
        if sequence[i-1] > sequence[i]:
            answer += i
            break
    print(answer)