import sys
sys.stdin = open('1388.txt')


def checkTile(tile, i, j):
    if tile == '-':
        while j < M and floor[i][j] == tile:
            visited[i][j] = True
            j += 1

    else:
        while i < N and floor[i][j] == tile:
            visited[i][j] = True
            i += 1


N, M = map(int, input().split())  # N:세로, M:가로
floor = [list(input()) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

cnt = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            cnt += 1
            visited[i][j] = True
            checkTile('-', i, j+1) if floor[i][j] == '-' else checkTile('|', i+1, j)


print(cnt)