import sys
import collections
input = sys.stdin.readline

def solution(N,K):
    in_deque = [0]*(N+1)
    graph = [[] for _ in range(N+1)]
    Time = [0] + list(map(int, input().split()))
    for i in range(K):
        x, y = map(int, input().split())
        graph[x].append(y)
        in_deque[y] +=1
    W = int(input())
    answer = 0
    while in_deque[W]:
        q = []
        result = 100001
        minimum = 0
        for i in range(1, N+1):
            if in_deque[i] == 0: #i가 갈 수 있다면
                q.append(i) #i를 데려가자!
                if result > Time[i]:
                    result = Time[i]
                    minimum = i
        answer += result
        for j in q:
            Time[j] -= result
        for i in graph[minimum]:
            in_deque[i] -=1
        in_deque[minimum] = -1 #완성 된 것은 더이상 쓰면 안된다.
    answer += Time[W]
    return answer
if __name__=="__main__":
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        print(solution(N,K))
