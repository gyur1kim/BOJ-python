import sys
sys.stdin = open('10162.txt')

T = int(input())
A = B = C = 0
if T % 10:
    print(-1)
else:
    t, T = divmod(T, 300)
    A = t
    t, T = divmod(T, 60)
    B = t
    t, T = divmod(T, 10)
    C = t
    print(A, B, C)

