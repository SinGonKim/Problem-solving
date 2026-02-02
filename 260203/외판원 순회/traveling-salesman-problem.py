

# Please write your code here.
def simulate(s, v):
    global visited, answer
    visited[s] = 1
    if sum(visited) == n:
        answer = max(answer, v)
        return

    for i in range(1,n):
        if visited[i] or not A[s][i]:continue
        visited[i] = 1
        simulate(i, v + A[s][i])
        visited[i] = 0
    



if __name__ == "__main__":
    n = int(input())
    A = [list(map(int, input().split())) for _ in range(n)]
    visited = [0 for _ in range(n)]
    answer = 0
    simulate(0, 0)
    print(answer)