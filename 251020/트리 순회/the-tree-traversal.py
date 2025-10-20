n = int(input())

graph = [[] for _ in range(27)]

for _ in range(n):
    x, l, r = input().split()
    if l != '.':
        graph[ord(x)-ord('A')].append(ord(l)-ord('A'))
    else:
        graph[ord(x)-ord('A')].append('.')
    
    if r != '.':
        graph[ord(x)-ord('A')].append(ord(r)-ord('A'))
    else:
        graph[ord(x)-ord('A')].append('.')
# Please write your code here.

def preorder(root):
    global pre
    visited[root] = 1
    pre.append(chr(ord('A') + root))
    if len(graph[root]) == 0:
        return
    if graph[root][0] != '.':
        preorder(graph[root][0])
    if graph[root][1] != '.':
        preorder(graph[root][1])

visited = [0 for _ in range(27)]
pre = []
preorder(0)
print("".join(pre))

def inorder(root):
    global en

    if len(graph[root]) and graph[root][0] != '.':
        inorder(graph[root][0])
    visited[root] = 1
    en.append(chr(ord('A') + root))

    if len(graph[root]) and graph[root][1] != '.':
        inorder(graph[root][1])
en = []
visited = [0 for _ in range(27)]
inorder(0)
print("".join(en))

def postorder(root):
    global post
    if len(graph[root]) and graph[root][0] != '.':
        postorder(graph[root][0])
    if len(graph[root]) and graph[root][1] != '.':
        postorder(graph[root][1])
    visited[root] = 1
    post.append(chr(ord('A') + root))
post = []
visited = [0 for _ in range(27)]
postorder(0)
print("".join(post))