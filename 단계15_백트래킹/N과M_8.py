import sys
sys.stdin = open('N과M_8.txt')


def combination(idx, depth):
    if depth == b:
        print(*ansLst)
        return

    for i in range(idx, a):
        ansLst.append(inputLst[i])
        combination(i, depth + 1)
        ansLst.pop()


a, b = map(int, input().split())
inputLst = list(map(str, sorted(list(map(int, input().split())))))
ansLst = []
combination(0, 0)