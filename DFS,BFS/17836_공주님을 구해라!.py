import sys
sys.stdin = open('17836.txt')

from collections import deque
def BFS(i, j):
    global findGram
    queue = deque([(i, j)])
    visited[i][j] = 1
    findGram = 10001

    while queue:
        i, j = queue.popleft()
        if visited[i][j] > T:  # 아직 탐색중인데 T를 넘어간다? gram을 찾았으면 gram 리턴, 아니면 바로 끝내버리기
            return 'Fail' if findGram > T else findGram

        # 탐색 시작해보자구
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = i + dx, j + dy
            if 0<=nx<N and 0<=ny<M and castle[nx][ny] != 1 and not visited[nx][ny]:
                # 다음 영역이 도착 지점이면?
                if nx == N-1 and ny == M-1:
                    # 칼을 찾았을 때 걸린 시간과 탐색하는 데 걸린 시간을 비교해 작은 값 리턴
                    return min(findGram, visited[i][j])
                # 갈 수 있는 길이면
                if castle[nx][ny] == 0:
                    # 큐에 넣고 방문 처리, 이전 값보다 한발짝 더 움직인거로 보자
                    visited[nx][ny] = visited[i][j] + 1
                    queue.append((nx, ny))
                # 검을 찾았다면?
                elif castle[nx][ny] == 2:
                    # 방문 처리하고, 최단거리 계산하기
                    visited[nx][ny] = visited[i][j] + 1
                    findGram = visited[nx][ny] + (N-nx-1) + (M-ny-1) - 1
    # 큐를 다 돌았는데 도착하지 못했다면... gram찾았는지 확인하고 fail 리턴하기
    return 'Fail' if findGram > T else findGram


N, M, T = map(int, input().split())  # 행, 렬, 제한 시간
castle = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

# directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
print(BFS(0, 0))
# for l in visited:
#     print(l)
