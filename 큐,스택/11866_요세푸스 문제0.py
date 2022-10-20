# 평범하게 queue로 푼 방식
'''
from collections import deque
queue = deque()
N, K = map(int, input().split())
for i in range(1, N+1):
    queue.append(i)

cnt = 1
ans = ''
while queue:
    x = queue.popleft()
    if cnt % K:
        queue.append(x)
    else:
        ans += str(x) + ', '
    cnt += 1

print(f'<{ans.rstrip(", ")}>')
'''


# 숏코딩
# 바다코끼리 연산자(:=)를 이용했다. 귀엽다. 바다코끼리 연산자란?
'''
왼쪽의 변수에 오른쪽의 표현을 값으로서 할당과 동시에 표현으로서의 기능을 수행
'''
n, k = map(int, input().split())
c, *a = range(n+1)

# for i in a[::-1]:
#     print(a)
#     c = (c+k-1) % i   # i는 현재 배열의 길이임!
#     print(a.pop(c))
'''
이 숏코딩은!!!
c는 아까 원소를 날린 인덱스를 나타낸다.
아까 위치에서 k-1만큼 더해주는 이유는 pop을 해서 하나가 줄었기 때문에 k-1이다!!
현재 배열의 길이로 나눠서, index에러를 방지한다!!!
똑똑하다..

배열을 str()로 만든 뒤 [1:-1]을 슬라이싱하면 대괄호가 사라진다. wow..
'''

print(f'<{str([a.pop(c := (c+k-1) % b)for b in a[::-1]])[1:-1]}>')


# shpark0913님
N, K = map(int, input().split())
arr = [i for i in range(1, N+1)]
arr2 = []
idx = K - 1

for i in range(N):
    idx = idx % len(arr)
    arr2.append(arr.pop(idx))
    idx += (K-1)

# print('<', end='')
# for i in range(len(arr2)-1):
#     print(f'{arr2[i]}, ', end='')
# print(f'{arr2[-1]}>')

print(f'<{str(arr2)[1:-1]}>')