import sys
sys.stdin = open('N과M_7.txt')


def product(depth):
    # if depth == b:
    #     print(*ansLst)
    #     return

    for i in range(a):
        ansLst.append(inputLst[i])
        if depth + 1 == b:
            print(*ansLst)
        else:
            product(depth + 1)
        ansLst.pop()



a, b = map(int, input().split())
inputLst = list(map(str, sorted(list(map(int, input().split())))))
# visited = [False] * a
ansLst = []
product(0)