n = int(input())
numbers = list(map(int, input().split(' ')))
prime = 0 # 소수의 개수

for i in numbers:
    cnt = 0 
    if(i == 1): # 1은 소수가 아니기 때문에 건너띔
        continue
    for j in range(2, i+1):
        if(i % j == 0):
            cnt += 1
    if(cnt == 1):
        prime += 1
print(prime)
