import sys
sys.stdin = open('1260.txt')


from collections import deque
def DFS(root):
    res = ''
    visited = [False] * (N + 1)
    stack = [root]

    while stack:
        root = stack.pop()
        if not visited[root]:
            res += str(root) + ' '
            visited[root] = True
            for v in sorted(graph[root], reverse=True):
                if not visited[v]:
                    stack.append(v)
    return res


def BFS(root):
    res = ''
    visited = [False] * (N + 1)
    queue = deque([root])
    visited[root] = True

    while queue:
        root = queue.popleft()
        res += str(root) + ' '
        for v in sorted(graph[root]):
            if not visited[v]:
                visited[v] = True
                queue.append(v)
    return res


N, M, V = map(int, input().split())  # N: 정점의 개수, M: 간선의 개수, V: 시작 노드
# graph = {}
#
# for m in range(M):
#     s, e = map(int, input().split())
#
#     tmp1 = graph.get(s, [])
#     graph[s] = tmp1 + [e]
#
#     tmp2 = graph.get(e, [])
#     graph[e] = tmp2 + [s]

graph = [list() for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    print(graph)
    graph[s].append(e)
    graph[e].append(s)

print(DFS(V))
print(BFS(V))