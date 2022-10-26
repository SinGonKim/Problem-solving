n = int(input())
cnt = 0
x = 666
while True:
    if '666' in str(x): #666이 있는지 하나씩 비교해보자
        cnt += 1
    if cnt == n: #원하던 순서 번호랑 같으면 출력!
        print(x)
        break
    x += 1
