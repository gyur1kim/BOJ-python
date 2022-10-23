import sys
sys.stdin = open('1874.txt')

N = int(input())
# 정석대로 풀어보자구~
stack = []
ans = ''
cnt = 0


# for _ in range(N):
#     n = int(input())
#     print(stack)
#     if stack:
#         if stack[-1] == n:
#             stack.pop()
#             ans += '-\n'
#         elif stack[-1] < n:
#             for i in range(cnt+1, n):
#                 stack.append(i)
#                 ans += '+\n'
#             ans += '+\n-\n'
#             cnt = n
#         else:
#             ans = 'NO'
#             break
#     else:
#         for i in range(cnt+1, n):
#             stack.append(i)
#             ans += '+\n'
#         ans += '+\n-\n'
#         cnt = n
# print(ans)

# readline쓰니까 시간이 1/25 줄었다!!
for _ in range(N):
    n = int(input())
    print(stack)
    if not stack or stack[-1] < n:
        for i in range(cnt + 1, n):
            stack.append(i)
            ans += '+\n'
        ans += '+\n-\n'
        cnt = n
    elif stack[-1] == n:
        stack.pop()
        ans += '-\n'
    else:
        ans = 'NO'
        break
print(ans)






