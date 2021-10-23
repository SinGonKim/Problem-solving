'''문제 https://www.acmicpc.net/problem/2447'''
def dfs(n):
    global graph
    if n==3:
        graph[0][:3] = graph[2][:3] =[1]*3
        graph [1][:3] = [1, 0, 1]
        return
    a = n//3
    dfs(a)
    for i in range(3):
        for j in range(3):
            if i==1 and j==1:
                continue
            for k in range(a):
                graph[a*i+k][a*j:a*(j+1)] = graph[k][:a]
if __name__ == "__main__":
    N = int(input())
    graph = [[0 for _ in range(N)] for _ in range(N)]
    dfs(N)
    for i in graph:
        for j in i:
            if j:
                print('*', end ='')
            else:
                print(' ', end='')
        print()
