import sys
sys.stdin = open('2178.txt')

from collections import deque
def searchMaze(i, j):
    queue = deque([(i, j)])

    while queue:
        i, j = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = i + dx, j + dy
            if 0<=nx<N and 0<=ny<M and maze[nx][ny] == 1:
                if nx == N-1 and ny == M-1:
                    return maze[i][j] + 2
                queue.append((nx, ny))
                maze[nx][ny] = maze[i][j] + 1


N, M = map(int, input().split())   #N: 세로, M: 가로
maze = [list(map(int, input())) for _ in range(N)]
maze[0][0] = 0
print(maze)
print(searchMaze(0, 0))

'''
원래 visited를 썼는데 메모리 줄여보고싶어서... maze의 값을 변경하는 방식으로 바꿨다.
근데 8KB밖에 안줄었다!!!

<< 원래 visited를 썼던 코드 >>
from collections import deque
def searchMaze(i, j):
    queue = deque([(i, j)])

    while queue:
        i, j = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = i + dx, j + dy
            if 0<=nx<N and 0<=ny<M and maze[nx][ny] == 1 and not visited[nx][ny]:
                if nx == N-1 and ny == M-1:
                    return visited[i][j] + 1
                queue.append((nx, ny))
                visited[nx][ny] = visited[i][j] + 1


N, M = map(int, input().split())   #N: 세로, M: 가로
maze = [list(map(int, input())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
visited[0][0] = 1
print(searchMaze(0, 0))
'''