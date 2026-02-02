import sys
INF = sys.maxsize

# Please write your code here.
def simulate(s, v):
    global visited, answer, order

    if sum(visited) == n:
        if A[s][0] == 0:
            return
        v += A[s][0]
        if answer > v:
            answer = v
            # print(order, answer)
        return

    for i in list(set([i for i in range(n)])-set(order)):
        if visited[i] or A[s][i] == 0:continue
        visited[i] = 1
        order.append(i)
        simulate(i, v + A[s][i])
        visited[i] = 0
        order.pop()


if __name__ == "__main__":
    n = int(input())
    A = [list(map(int, input().split())) for _ in range(n)]
    visited = [0 for _ in range(n)]
    order = [0]
    answer = INF
    visited[0] = 1
    simulate(0, 0)
    print(answer)