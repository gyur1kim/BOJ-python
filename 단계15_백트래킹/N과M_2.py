import sys
sys.stdin = open('N과M_2.txt')

def combination(n, depth):
    if depth == b:
        print(*lst)
    for i in range(n, a+1):
        if i not in lst:
            lst.append(i)
            combination(i+1, depth + 1)
            lst.pop()


a, b = map(int, input().split())
lst = []
combination(1, 0)