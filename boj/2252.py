import sys
import collections
input = sys.stdin.readline
N, M = map(int, input().split())
B = [0]*(N+1) #숫자가 0이면 바로 시작해도 된다는 뜻이고 1이면 앞에 하나가 가야 갈 수 있다는 뜻
A = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    A[a].append(b) #a가 가면 b는 해방!
    B[b] +=1 #b 는 a가 가야 갈 수 있다는 뜻
result = []
q = collections.deque()
for i in range(1, N+1):
    if B[i] == 0: #i가 갈 수 있다면
        q.append(i) #i를 데려가자!
while q:
    node = q.popleft()
    result.append(node) #결과 순서를 만들자!
    for i in A[node]: #node가 결과에 들어왔으니 뒤에 올 수 있는 나머지 원소들은 node에게서 해방!
        B[i] -= 1 #근데 node에게서 해방아지 나머지한테 해방인지는 봐야한다.
        if B[i] == 0: #완전한 해방이면
            q.append(i) #q로 들어오는 것을 환영한다!
for i in result: #result에 들어온 순서대로 출력한다!
    print(i, end =' ')
