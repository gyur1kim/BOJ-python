import sys
sys.stdin = open('11725.txt')

# 이게 이진트리가 아니었다ㅋㅋ
'''
class Node():
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent


N = int(input())  # 노드의 개수
nodeDict = {1: Node(1, None)}
for n in range(N-1):
    a, b = map(int, input().split())
    if a in nodeDict:  # a가 부모 노드
        nodeDict[b] = Node(b, a)
    else:  # b가 부모 노드
        nodeDict[a] = Node(a, b)

for i in range(2, N+1):
    if i not in nodeDict:
        continue
    else:
        print(nodeDict[i].parent)
'''

'''
문제를 어떻게 해결하면 좋을까!!!
1. list를 이용하자, idx는 부모, 값에는 자식들을 담자.
2. 누가 부모인지 자식인지 모르겠으면, 임시 딕셔너리에 넣어놓자.
3. 다음에, list에서 BFS를 이용하며 부모자식을 탐색하자...?
'''

from collections import deque

def BFS(root):
    queue = deque([root])
    while queue:
        node = queue.popleft()
        for childNode in treeDict[node]:
            if not visited[childNode]:
                visited[childNode] = True
                ans[childNode] = node
                queue.append(childNode)


V = int(input())
treeDict = {}
for i in range(1, V+1):
    treeDict[i] = []
for _ in range(V-1):
    a, b = map(int, input().split())
    treeDict[a].append(b)
    treeDict[b].append(a)
visited = [False] * (V+1)
ans = [0] * (V+1)
BFS(1)
print('\n'.join(map(str, ans[2:])))