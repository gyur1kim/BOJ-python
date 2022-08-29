import sys
sys.stdin = open('10833.txt')

N = int(input())
restApple = 0
for _ in range(N):
    students, apple = map(int, input().split())
    restApple += apple%students

print(restApple)