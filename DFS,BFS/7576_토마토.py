import sys
sys.stdin = open('7576.txt')


# 방법 1. 토마토의 위치를 좌표로 받는다
'''
from collections import deque
M, N = map(int, input().split())  # M: 가로, N: 세로
box = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
queue = deque()     # BFS 탐색을 할 큐
tomatoCoord = set()   # 토마토들의 좌표를 저장할 셋(나중에 탐색이 끝나도 좌표가 남아있으면 -1 출력할거임


for i in range(N):
    for j in range(M):
        if box[i][j] == 1:          # 익은 토마토가 존재하면
            queue.append((i, j))    # 큐에 넣고 좌표값도 저장하기
            tomatoCoord.add((i, j))
            visited[i][j] = 1
        elif box[i][j] == -1:
            visited[i][j] = -1
        else:
            tomatoCoord.add((i, j))

day = 0
if not queue:
    print(-1)
else:
    while queue:
        i, j = queue.popleft()
        tomatoCoord.remove((i, j))  # 방문한 곳의 좌표 빼기
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = i+dx, j+dy
            if 0<=nx<N and 0<=ny<M and visited[nx][ny] == 0:
                day = visited[i][j]
                queue.append((nx, ny))
                visited[nx][ny] = visited[i][j] + 1
    if not tomatoCoord:
        print(day)
    else:
        print(-1)
'''


# 방법 2. 토마토의 개수를 세자
# => set에서 하나씩 remove하는 방식보다 시간이 거의 1/3 감축됐다.....WOW
'''
from collections import deque
M, N = map(int, input().split())  # M: 가로, N: 세로
box = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
tomatoes = 0   # 덜 익은 토마토의 개수
queue = deque()     # BFS 탐색을 할 큐


for i in range(N):
    for j in range(M):
        if box[i][j] == 1:          # 익은 토마토가 존재하면
            queue.append((i, j))    # 큐에 넣기, 방문 처리
            visited[i][j] = 1
        elif box[i][j] == -1:
            visited[i][j] = -1
        else:
            tomatoes += 1

day = 0
if not queue:   # 익은 토마토가 없음
    print(-1)
else:           # 익은 토마토가 있음!! BFS 시작
    while queue:
        i, j = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = i+dx, j+dy
            if 0<=nx<N and 0<=ny<M and visited[nx][ny] == 0:
                day = visited[i][j]
                tomatoes -= 1             # 안 익었던 토마토의 개수 -1
                queue.append((nx, ny))
                visited[nx][ny] = visited[i][j] + 1
        # if tomatoes == 0:   # 덜 익은 토마토가 0이 되면 바로 break해버리면? 빨라질까? => 딱히 유의미하지는 않았다.
        #     break

    if not tomatoes:   # 토마토가 0이면?
        print(day)
    else:
        print(-1)
'''


# 방법 3. visited가 없어도 될 것 같은데...
# => visited를 안쓰니까 시간도 조오오금 줄고(20ms, 무엇보다 메모리가 엄청 줄었다)
from collections import deque
M, N = map(int, input().split())  # M: 가로, N: 세로
box = [list(map(int, input().split())) for _ in range(N)]
tomatoes = 0   # 덜 익은 토마토의 개수
queue = deque()     # BFS 탐색을 할 큐

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:          # 익은 토마토가 존재하면
            queue.append((i, j))    # 큐에 넣기
        elif box[i][j] == 0:
            tomatoes += 1

day = 0
if not queue:   # 익은 토마토가 없음!! 익을 수가 없으니 -1 출력
    print(-1)
else:           # 익은 토마토가 있음!! BFS 시작
    while queue:
        i, j = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = i+dx, j+dy
            if 0<=nx<N and 0<=ny<M and box[nx][ny] == 0:
                day = box[i][j]
                tomatoes -= 1             # 안 익었던 토마토의 개수 -1
                queue.append((nx, ny))
                box[nx][ny] = box[i][j] + 1
    if not tomatoes:   # 토마토가 0이면?
        print(day)
    else:              # 토마토가 0이 아니면?
        print(-1)



# 결론
'''
마지막엔 input = sys.stdin.readline을 사용하는 방식으로 시간을 380ms까지 줄일 수 있었다.
거의 1/10을 줄였다. 초반엔 3532ms였으니깐.. 물론 메모리도 visited를 쓰지 않는 방식으로 많이 줄였다.
거의 50000KB를 줄였다. 굳

무조건 visited를 사용해서 풀지 말고, 생각을 정리한 뒤 효율적으로 문제를 해결하는 습관을 들어야할 듯 하다..
'''