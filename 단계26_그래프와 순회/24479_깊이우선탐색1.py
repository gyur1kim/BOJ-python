'''
5 5 1
1 4
1 2
2 3
2 4
3 4

'''

# 내가 생각했던 DFS인데....
# 방문 순서를 저장하는 방법을 더 간결하게 할 수 있다.
'''
def DFS(root, depth):
    stack = [root]

    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = depth
            depth += 1
        nodes = sorted(graph[v], reverse=True)
        for node in nodes:
            if not visited[node]:
                stack.append(node)
'''

def DFS(start):
    stack = [start]
    depth = 1

    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = depth
            depth += 1
            stack += sorted(graph[node], reverse=True)


N, M, root = map(int, input().split())   # 정점의 수, 간선의 수, 시작 정점
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (N+1)
DFS(root)
print('\n'.join(map(str, visited[1:])))