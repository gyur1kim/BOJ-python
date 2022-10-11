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
            for v in sorted(graph.get(root, []), reverse=True):
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
        for v in sorted(graph.get(root, [])):
            if not visited[v]:
                visited[v] = True
                queue.append(v)
    return res


N, M, V = map(int, input().split())  # N: 정점의 개수, M: 간선의 개수, V: 시작 노드
graph = {}

for m in range(M):
    s, e = map(int, input().split())
    tmp1 = graph.get(s, [])
    graph[s] = tmp1 + [e]
    tmp2 = graph.get(e, [])
    graph[e] = tmp2 + [s]

# graph = [list() for _ in range(N+1)]
# for _ in range(M):
#     s, e = map(int, input().split())
#     print(graph)
#     graph[s].append(e)
#     graph[e].append(s)

print(DFS(V))
print(BFS(V))


# 리스트에 노드들의 정보를 담는 방법과 딕셔너리에 노드들의 정보를 담는 방법!!
# 그렇게 유의미한 차이는 없다. 시간 복잡도와 공간 복잡도의 트레이드 오프같은 느낌..