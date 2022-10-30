from collections import deque
import sys
input = sys.stdin.readline

if __name__ =="__main__":
    T = int(input())
    for _ in range(T):
        p = str(input().strip())
        n = int(input())
        a = str(input().strip())
        if len(a)>2:
            s= a[1:-1]
            deq = deque(map(int,s.split(',')))
        else:
            deq = deque()
        e = 0
        r = 0 #리버스를 계속 하면 시간복잡도가 많이 커지므로 횟수를 세서 나중에 홀수가 나올때만 reverse하도록 한다. 수를 뺄때는 짝수일때 popleft, 홀수일때 반대로 pop
        for func in p:
            if func == "R":
                r +=1
            if func == "D":
                if len(deq) == 0:
                    print("error")
                    e = 1
                    break
                elif r%2 == 0:
                    deq.popleft()
                elif r%2 == 1:
                    deq.pop()
        if r%2 == 1:
            deq.reverse()
        if e!=1:
            ans = list(deq)
            print('[', end='')
            print(','.join(map(str,ans)), end ='')
            print(']')

