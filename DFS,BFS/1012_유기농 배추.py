import sys
sys.stdin = open('1012_input.txt')

for _ in range(int(input())):
    M, N, K = map(int, input().split())  # M: 가로 길이, N: 세로 길이, K: 배추의 위치

    field = [[0]*M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for _ in range(K):
        j, i = map(int, input().split())
        field[i][j] = 1

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    stack = []
    bugs = 0
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1 and not visited[i][j]:
                bugs += 1
                stack.append((i, j))

                while stack:
                    a, b = stack.pop()
                    visited[a][b] = True
                    for d in range(4):
                        nx, ny = a + directions[d][0], b + directions[d][1]
                        if 0<=nx<N and 0<=ny<M and field[nx][ny] == 1 and not visited[nx][ny]:
                            stack.append((nx, ny))
    print(bugs)