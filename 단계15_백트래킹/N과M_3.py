import sys
sys.stdin = open('N과M_3.txt')

def permutation_H(depth):
    if depth == b:
        print(*lst)
        return

    for i in range(1, a+1):
        lst.append(i)
        permutation_H(depth+1)
        lst.pop()


a, b = map(int, input().split())
lst = []
permutation_H(0)


